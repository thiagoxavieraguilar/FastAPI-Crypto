venv:
	python -m venv venv

activate:
	venv\Scripts\activate

install:
	pip install -r docs/requirements.txt

format:
	black .

test:
	pytest tests/

run:
	python backend/main.py
