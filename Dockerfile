FROM docker.io/python:3.8-alpine3.13

COPY app /app
WORKDIR /app

#CMD ["uvicorn", "main:app", "--reload"]
CMD ["python", "./main.py"]
