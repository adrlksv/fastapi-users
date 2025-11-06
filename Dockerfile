FROM python:3.12-bookworm

ENV PYTHONDONTBYTECODE=1

WORKDIR /app

COPY pyproject.toml /app/

COPY poetry.lock /app/

RUN pip install poetry

RUN poetry install --no-root --no-ansi 