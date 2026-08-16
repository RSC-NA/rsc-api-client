#!/usr/bin/env bash
#
# Regenerate the rscapi client from the upstream OpenAPI spec, bumping the
# package version so downstream consumers can tell that something changed.
#
# The spec's own info.version ("v1") is the API *contract* version and stays
# put; this script moves packageVersion, which is the Python client's version.
#
# Usage: scripts/regenerate.sh [--patch|--minor|--major] [-f|--force]
#
# --force (or FORCE=1 via the Makefile) regenerates even when the upstream spec
# is byte-identical to the committed snapshot. Note this is *our* gate, not the
# generator's: openapi-generator has no --force flag and always overwrites what
# it emits, so forcing only re-runs it (useful after a generator version bump,
# a template change, or hand-edits that need to be blown away).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC_SRC="${SPEC_SRC:-$ROOT/../web-rsc-website/openapi/openapi.json}"
SNAPSHOT="$ROOT/openapi/openapi.json"

BUMP=patch
FORCE="${FORCE:-0}"
for arg in "$@"; do
  case "$arg" in
    --major|--minor|--patch) BUMP="${arg#--}" ;;
    -f|--force) FORCE=1 ;;
    -h|--help) sed -n '3,15p' "${BASH_SOURCE[0]}" | sed 's/^# \?//'; exit 0 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

[[ -f "$SPEC_SRC" ]] || { echo "spec not found: $SPEC_SRC" >&2; exit 1; }

# Gate: skip the whole run when the upstream spec is byte-identical to the
# snapshot that produced the current client.
if [[ -f "$SNAPSHOT" ]] && cmp -s "$SPEC_SRC" "$SNAPSHOT"; then
  if [[ $FORCE -eq 0 ]]; then
    echo "Spec unchanged; nothing to do. (make update FORCE=1 to regenerate anyway)"
    exit 0
  fi
  echo "Spec unchanged; forcing regeneration."
fi

CUR=$(python3 -c 'import re,sys; print(re.search(r"^version\s*=\s*\"([^\"]+)\"", open(sys.argv[1]).read(), re.M).group(1))' "$ROOT/pyproject.toml")
NEW=$(python3 -c '
import sys
ma, mi, pa = (int(x) for x in sys.argv[1].split("."))
b = sys.argv[2]
if b == "major": ma, mi, pa = ma + 1, 0, 0
elif b == "minor": mi, pa = mi + 1, 0
else: pa += 1
print(f"{ma}.{mi}.{pa}")' "$CUR" "$BUMP")

echo "Version: $CUR -> $NEW ($BUMP)"

# The generator is the npm wrapper (@openapitools/openapi-generator-cli); the
# jar version it runs is pinned in openapitools.json, NOT by the wrapper's own
# version. Bump it with:
#
#   openapi-generator-cli version-manager set <x.y.z>
#
# Never `set latest` -- Maven's search API lags badly and has silently pinned
# this repo backwards before. Check the real list at
# https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/maven-metadata.xml
#
# The wrapper is a global npm package under the *current* node version, so it
# disappears if you nvm-switch. There is also a PyPI package with the identical
# command name; if one gets installed it shadows this and ignores
# openapitools.json entirely. Hence the check.
command -v openapi-generator-cli >/dev/null \
  || { echo "ERROR: openapi-generator-cli not on PATH (nvm switched? run: npm i -g @openapitools/openapi-generator-cli)" >&2; exit 1; }

PINNED=$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["generator-cli"]["version"])' "$ROOT/openapitools.json")
ACTIVE=$(openapi-generator-cli --openapitools "$ROOT/openapitools.json" version 2>/dev/null | tail -1)
[[ "$ACTIVE" == "$PINNED" ]] || {
  echo "ERROR: openapitools.json pins $PINNED but $(command -v openapi-generator-cli) reports '$ACTIVE'." >&2
  echo "       Something is shadowing the npm wrapper (a PyPI openapi-generator-cli?)." >&2
  exit 1
}
echo "Generator: $ACTIVE"

openapi-generator-cli --openapitools "$ROOT/openapitools.json" generate \
  -i "$SPEC_SRC" \
  -g python \
  -o "$ROOT" \
  --library asyncio \
  --git-user-id RSC-NA \
  --git-repo-id rsc-api-client \
  --additional-properties="packageName=rscapi,projectName=rscapi,packageVersion=$NEW,hideGenerationTimestamp=true"

mkdir -p "$(dirname "$SNAPSHOT")"
cp "$SPEC_SRC" "$SNAPSHOT"

# Relax the generator's aiohttp floor.
#
# The python generator hardcodes whatever aiohttp was current when its template
# was cut (7.18.0 emits >=3.13.5). Our main consumer is a Red-DiscordBot cog,
# and Red 3.5.24 pins aiohttp==3.9.5 *exactly* -- a floor above that makes
# rscapi flatly uninstallable next to it ("your project's requirements are
# unsatisfiable").
#
# Nothing in the generated client needs the newer aiohttp: rest.py only touches
# ClientSession(connector=/trust_env=/trace_configs=) and
# TCPConnector(limit=/limit_per_host=/ssl=), all of which exist in 3.8.x. So the
# floor is packaging noise, and we rewrite it after every generate.
#
# Raise it with AIOHTTP_MIN=x.y.z if Red ever unpins.
AIOHTTP_MIN="${AIOHTTP_MIN:-3.8.4}"
sed -i -E "s/\"aiohttp \(>=[0-9][0-9a-z.]*\)\"/\"aiohttp (>=$AIOHTTP_MIN)\"/" "$ROOT/pyproject.toml"
sed -i -E "s/^aiohttp >= [0-9][0-9a-z.]*$/aiohttp >= $AIOHTTP_MIN/" "$ROOT/requirements.txt"
sed -i -E "s/\"aiohttp >= [0-9][0-9a-z.]*\"/\"aiohttp >= $AIOHTTP_MIN\"/" "$ROOT/setup.py"

for f in pyproject.toml requirements.txt setup.py; do
  grep -q "aiohttp[ (]*>= *$AIOHTTP_MIN" "$ROOT/$f" \
    || { echo "ERROR: aiohttp floor rewrite missed $f (generator changed the line format?)" >&2; exit 1; }
done
echo "aiohttp floor: >=$AIOHTTP_MIN"

# Fail loudly if packageVersion did not reach the generated code -- this is the
# one thing the whole script exists to guarantee.
grep -q "__version__ = \"$NEW\"" "$ROOT/rscapi/__init__.py" \
  || { echo "ERROR: packageVersion did not reach rscapi/__init__.py" >&2; exit 1; }

echo
echo "Regenerated rscapi $NEW"
git -C "$ROOT" status --short | head -40

# A spec that gained a schema produces model files git has never seen. `git commit -am`
# stages tracked modifications only, so those files stay behind while the regenerated
# rscapi/models/__init__.py that imports them goes out -- which is how v2.1.2 shipped a
# tree where `import rscapi` raised ModuleNotFoundError. Call it out by name, because
# the status listing above scrolls and a `??` is easy to read past.
NEW_FILES=$(git -C "$ROOT" ls-files --others --exclude-standard -- rscapi/ | head -40)
if [ -n "$NEW_FILES" ]; then
  echo
  echo "NOTE: these generated files are new and are NOT staged by 'git commit -a':"
  echo "$NEW_FILES" | sed 's/^/  /'
fi

echo
echo "Next: review the diff, run 'make test', then:"
# git add -A, not commit -am: -a would drop the new files listed above.
# git tag -a, not a bare git tag: --follow-tags pushes annotated tags only, so every
# lightweight tag this script suggested stayed on the machine that cut it. v1.1.0
# through v2.1.1 were all stranded that way and never reached the remote.
echo "  git add -A && git commit -m \"rscapi $NEW\" && git tag -a \"v$NEW\" -m \"rscapi $NEW\" && git push --follow-tags"
