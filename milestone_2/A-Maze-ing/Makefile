NAME	= a_maze_ing
CONFIG	= config.txt

all: install

install:
	pip3 install poetry
	poetry install

run:
	poetry run python3 $(NAME).py $(CONFIG)

build:
	poetry build

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

fclean: clean
	rm -rf dist/
	rm -rf .venv/

re: fclean all

.PHONY: all install run build clean fclean re