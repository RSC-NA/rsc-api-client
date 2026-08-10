#!/usr/bin/env bash
#
# Regenerate the rscapi client from the upstream OpenAPI spec, bumping the
# package version so downstream consumers can tell that something changed.
#
# The spec's own info.version ("v1") is the API *contract* version and stays
# put; this script moves packageVersion, which is the Python client's version.
#
# Usage: scripts/regenerate.sh [--patch|--minor|--major] [--force]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SPEC_SRC="${SPEC_SRC:-$ROOT/../web-rsc-website/openapi/openapi.json}"
SNAPSHOT="$ROOT/openapi/openapi.json"

BUMP=patch
FORCE=0
for arg in "$@"; do
  case "$arg" in
    --major|--minor|--patch) BUMP="${arg#--}" ;;
    --force) FORCE=1 ;;
    *) echo "unknown arg: $arg" >&2; exit 2 ;;
  esac
done

[[ -f "$SPEC_SRC" ]] || { echo "spec not found: $SPEC_SRC" >&2; exit 1; }

# Gate: skip the whole run when the upstream spec is byte-identical to the
# snapshot that produced the current client.
if [[ $FORCE -eq 0 && -f "$SNAPSHOT" ]] && cmp -s "$SPEC_SRC" "$SNAPSHOT"; then
  echo "Spec unchanged; nothing to do. (--force to regenerate anyway)"
  exit 0
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

openapi-generator-cli generate \
  -i "$SPEC_SRC" \
  -g python \
  -o "$ROOT" \
  --library asyncio \
  --git-user-id RSC-NA \
  --git-repo-id rsc-api-client \
  --additional-properties="packageName=rscapi,projectName=rscapi,packageVersion=$NEW,hideGenerationTimestamp=true"

mkdir -p "$(dirname "$SNAPSHOT")"
cp "$SPEC_SRC" "$SNAPSHOT"

# Fail loudly if packageVersion did not reach the generated code -- this is the
# one thing the whole script exists to guarantee.
grep -q "__version__ = \"$NEW\"" "$ROOT/rscapi/__init__.py" \
  || { echo "ERROR: packageVersion did not reach rscapi/__init__.py" >&2; exit 1; }

echo
echo "Regenerated rscapi $NEW"
git -C "$ROOT" status --short | head -40
echo
echo "Next: review the diff, run 'make test', then:"
echo "  git commit -am \"rscapi $NEW\" && git tag \"v$NEW\" && git push --follow-tags"
