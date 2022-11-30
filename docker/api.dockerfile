FROM python:3.9-buster

# Set workdir

WORKDIR /app

# Install system dependencies

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev

# Install python requirements

RUN python -m pip install -U pip

COPY requirements.txt ./
COPY requirements_dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files

COPY . .
