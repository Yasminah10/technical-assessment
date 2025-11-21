# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies including Tesseract
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libgl1-mesa-glx \
    libglib2.0-0 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install NumPy < 2.0 first to avoid conflicts
RUN pip install --no-cache-dir "numpy<2.0"

# Install other Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the notebook and app files
COPY ocr_model.ipynb .
COPY app.py .

# Expose port for Gradio
EXPOSE 7861

# Set environment variable for Gradio
ENV GRADIO_SERVER_NAME="0.0.0.0"

# Run the application
CMD ["python", "app.py"]
