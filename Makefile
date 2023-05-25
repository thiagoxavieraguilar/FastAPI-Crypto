clean:
	@find . -type d -name __pycache__ -exec rm -rf {} +

install:
	pip install -r docs/requirements.txt

run:
	python main.py
