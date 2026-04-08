.PHONY: install build package-install lint lint-fix

install:
    uv sync

build:
    uv build

package-install:
    uv tool install --force dist/*.whl

lint:
    uv run ruff check .

lint-fix:
    uv run ruff check VD_games --fix
