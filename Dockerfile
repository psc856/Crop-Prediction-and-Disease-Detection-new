# ---------------------------
# Base image: Python 3.11 slim
# ---------------------------
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# ---------------------------
# Install system dependencies for Pillow, TensorFlow, etc.
# ---------------------------
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# ---------------------------
# Copy requirements.txt first (caching layer)
# ---------------------------
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ---------------------------
# Copy the rest of the application
# ---------------------------
COPY . .

# Create upload folder (your Flask app uses it)
RUN mkdir -p static/uploads

# Expose the port App Runner expects
EXPOSE 8080

# ---------------------------
# Start the Flask app with Gunicorn
# ---------------------------
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
