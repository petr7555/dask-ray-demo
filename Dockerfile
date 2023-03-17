ARG PYTHON_VERSION=3.9
FROM python:$PYTHON_VERSION

LABEL name="python-$PYTHON_VERSION"
LABEL version="$PYTHON_VERSION"
LABEL maintainer="Petr Janik <peta.janik@email.cz>"

ARG POETRY_VERSION=1.2.2

# Install Poetry system-wide using pip
RUN pip install --upgrade pip && \
    pip install poetry==${POETRY_VERSION} 

WORKDIR /app

COPY pyproject.toml poetry.lock ./

ENV POETRY_VIRTUALENVS_IN_PROJECT=true
RUN poetry install --only main --no-root --no-cache --no-interaction

COPY app ./app
