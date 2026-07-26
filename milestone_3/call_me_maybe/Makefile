
install:
	@uv sync
# 	@uv add flake8
# 	@uv add mypy

run:
	@uv run python3 -m src

debug:
	@uv run python3 -m pdb -m src

lint:
	@uv run flake8 . --exclude=llm_sdk,.venv
	@uv run mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

clean:
	@rm -rf **/__pycache__ .mypy_cache

.PHONY: install run debug lint clean