FROM docker.io/python:3.9-alpine3.13

COPY app /app
WORKDIR /app

#CMD ["uvicorn", "main:app", "--reload"]
CMD ["python", "./main.py"]
