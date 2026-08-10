SPEC ?= ../web-rsc-website/openapi/openapi.json

.DEFAULT_GOAL := help
.PHONY: help check update update-minor update-major test

help: ## Show available make targets.
	@printf '%s\n\n' 'Usage: make <target> [SPEC=path/to/openapi.json]'
	@printf '%s\n' 'Targets:'
	@awk 'BEGIN {FS = ":.*## "} /^[[:alnum:]_-]+:.*## / {printf "  %-14s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

check: ## Report whether the upstream spec differs from the committed snapshot.
	@cmp -s $(SPEC) openapi/openapi.json && echo "up to date" || echo "spec changed - run 'make update'"

update: ## Regenerate the client with a patch version bump.
	@SPEC_SRC=$(abspath $(SPEC)) ./scripts/regenerate.sh

update-minor: ## Regenerate with a minor bump (endpoints added/removed).
	@SPEC_SRC=$(abspath $(SPEC)) ./scripts/regenerate.sh --minor

update-major: ## Regenerate with a major bump (/api/v1 superseded).
	@SPEC_SRC=$(abspath $(SPEC)) ./scripts/regenerate.sh --major

# The 240 generated tests are stubs with commented-out bodies -- none of them
# assert anything, so this is really an import smoke check over every generated
# module. That is still worth running: it is what surfaced the broken models
# excluded below.
#
# pytest lives in [tool.poetry.group.dev.dependencies], which uv doesn't read,
# and pyproject.toml is regenerated on every run so we can't move it there.
# Layer the dev tools on with --with instead of editing generated config.
#
# Excluded: three orphan models the generator emits broken and that nothing
# exports (see BROKEN_MODELS below). Drop the --ignore flags to re-check them.
BROKEN_MODELS = null_enum stats_dict_field team_game_list_results_field

test: ## Run the import smoke check over the generated modules.
	uv run --with pytest --with pytest-cov pytest --cov=rscapi \
		$(foreach m,$(BROKEN_MODELS),--ignore=test/test_$(m).py)
