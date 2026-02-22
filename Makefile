install:
	uv sync

VD-games:
	uv run start-game

build:
	uv build

package-install:
	uv tool install dist/*.whl
