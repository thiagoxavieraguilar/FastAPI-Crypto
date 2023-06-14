.PHONY: venv activate install format test

venv:
	poetry install

activate:
	poetry shell

install:
	poetry install

format:
	poetry run black .
	poetry run isort .

test:
	poetry run pytest tests/
