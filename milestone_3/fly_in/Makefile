# path=maps/easy/01_linear_path.txt
# path=maps/easy/02_simple_fork.txt
path=maps/challenger/01_the_impossible_dream.txt
# path=maps/hard/01_maze_nightmare.txt
.PHONY: install run debug lint clean

run:
	@uv run python3 -m src $(path)

install:
	uv sync

debug:
	uv run python3 -m pdb src

lint:
	@uv run flake8 . --exclude=.venv
	@uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs


clean:
	@rm -rf **/**/__pycache__ **/__pycache__ .mypy_cache .venv