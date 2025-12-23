FROM python:3.9-slim

# Install system libraries for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Environment variables to force port 7860
ENV PORT=7860
ENV HOST=0.0.0.0

EXPOSE 7860

# Start command with Proxy headers allowed
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860", "--forwarded-allow-ips", "*"
