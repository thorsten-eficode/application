FROM docker.io/python:3.9-alpine3.13

COPY requirements.txt /requirements.txt

RUN pip install --progress-bar off -r /requirements.txt

COPY src /app
WORKDIR /app

CMD ["uvicorn", "main:app", "--reload"]