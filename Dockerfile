ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install dependencies using Poetry
RUN poetry install --no-root

# Copy the source code into the container.
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD poetry run uvicorn app.main:app --reload --port 8000 --host 0.0.0.0