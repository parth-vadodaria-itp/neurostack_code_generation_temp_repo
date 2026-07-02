# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY calculator.py .
COPY main.py .
COPY test_calculator.py .
COPY requirements.txt .
COPY README.md .

# Create non-root user for security
RUN useradd -m -u 1000 calcuser && \
    chown -R calcuser:calcuser /app

# Switch to non-root user
USER calcuser

# Run tests to verify installation
RUN python -m unittest test_calculator.py

# Set entrypoint to run the calculator
ENTRYPOINT ["python", "main.py"]
