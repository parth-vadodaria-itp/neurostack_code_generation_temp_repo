# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY hello_2026.py .

# Copy requirements (even though empty, good practice)
COPY requirements.txt .

# Install dependencies (none in this case, but keeping for consistency)
RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user for security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Run the script
CMD ["python", "hello_2026.py"]
