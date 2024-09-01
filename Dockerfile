# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY ./api /app/api
COPY ./string_calculator /app/string_calculator

CMD ["uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8000"]
