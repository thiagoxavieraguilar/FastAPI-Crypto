run:
	python -m venv venv
	venv\Scripts\activate
	pip install -r docs/requirements.txt

format:
	black .

test:
	pytest tests/

build:
	docker build -t fastapi-app-crypto .

compose-up:
	docker-compose up

