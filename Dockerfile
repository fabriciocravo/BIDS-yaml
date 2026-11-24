# Base image - start from a container with python
FROM python:3.12-slim

# Installs git, curlm, and CA certificates (HTTPS - we need to install online things)
RUN apt-get update && apt-get install -y --no-install-recommends git curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Installs Deno for the validator
RUN curl -fsSL https://deno.land/install.sh | DENO_INSTALL=/usr/local sh

# Creates a local working directory
WORKDIR /app

# Copies the repo into the container
COPY . .
RUN pip install -r requirements.txt
