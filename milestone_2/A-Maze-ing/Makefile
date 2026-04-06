NAME	= a_maze_ing
CONFIG	= config.txt

all: install

install:
	pipx install uv
	uv run pip3 install mazegen-0.1.0-py3-none-any.whl --target .
	uv sync

run:
	uv run python3 $(NAME).py $(CONFIG)

build:
	uv build

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf mazegen-0.1.0.dist-info

fclean: clean
	rm -rf dist/
	rm -rf .venv/

re: fclean all

.PHONY: all install run build clean fclean re
