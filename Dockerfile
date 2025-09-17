# Use lightweight Python base (Debian slim)
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for Pillow, TensorFlow, etc.
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose the port App Runner expects
EXPOSE 8080

# Start Flask with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
