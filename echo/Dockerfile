FROM docker.io/python:3.8-alpine3.13

RUN addgroup --gid 250321 --system appgroup \
    && adduser --uid 250321 --system appuser --ingroup appgroup

COPY --chown=appuser:appgroup . /app

WORKDIR /app

USER appuser

CMD ["python", "./echo.py"]
