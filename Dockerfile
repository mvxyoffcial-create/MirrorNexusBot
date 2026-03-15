FROM python:3.11-slim

# System deps: ffmpeg, aria2c, 7zip, unrar, zip
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    p7zip-full \
    unrar-free \
    zip \
    unzip \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install rclone
RUN curl https://rclone.org/install.sh | bash

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create downloads dir
RUN mkdir -p /tmp/downloads

CMD ["python", "main.py"]
