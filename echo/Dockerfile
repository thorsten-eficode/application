FROM docker.io/python:3.8-alpine3.13

LABEL \
    org.opencontainers.image.created="2021-04-16 16:47:12" \
    org.opencontainers.image.authors="" \
    org.opencontainers.image.url="https://github.com/thorsten-eficode/application" \
    org.opencontainers.image.documentation="https://github.com/thorsten-eficode/application" \
    org.opencontainers.image.source="https://github.com/thorsten-eficode/application" \
    org.opencontainers.image.version="0.1.0" \
    org.opencontainers.image.revision="<COMMIT_SHA>" \
    org.opencontainers.image.vendo="thosten-eficode" \
    org.opencontainers.image.licenses="t.b.d." \
    org.opencontainers.image.ref.name="t.b.d."

RUN addgroup --gid 250321 --system appgroup \
    && adduser --uid 250321 --system appuser --ingroup appgroup

COPY --chown=appuser:appgroup . /app

WORKDIR /app

USER appuser

CMD ["python", "./echo.py"]
