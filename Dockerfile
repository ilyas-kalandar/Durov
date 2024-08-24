# Setup last version of python
FROM python:3.12-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Poetry setup
RUN curl -sSL https://install.python-poetry.org | python3 -

# Setup path for poetry
ENV PATH="/root/.local/bin:$PATH"

# Setup
WORKDIR /DUROV

# Copy requirements
COPY pyproject.toml poetry.lock* ./

# Setup deps
RUN poetry install

# Copy project's files
COPY . .

# For logs
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/DUROV/src

# Run application
CMD ["poetry", "run", "python", "-m", "durov"]