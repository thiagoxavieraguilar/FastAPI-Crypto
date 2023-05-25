FROM python:3.11

WORKDIR /app

COPY . /app

COPY docs/requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
