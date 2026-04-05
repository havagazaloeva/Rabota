.PHONY: install build package-install lint

install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check .
