install:
	uv sync
VD-games:
	uv run VD-games
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check VD_games
lint-fix:
	uv run ruff check VD_games --fix
