FROM python:3.12-bookworm

PYTHONDONTBYTECODE

WORKDIR /app

COPY pyproject.toml /app/

COPY poetry.lock /app/

RUN pip install poetry

RUN poetry install --no-root --no-ansi 