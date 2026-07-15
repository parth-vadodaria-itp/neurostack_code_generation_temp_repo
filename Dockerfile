# syntax=docker/dockerfile:1
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the application source.
COPY . .

# Run as a non-root user.
RUN addgroup --system app \
    && adduser --system --ingroup app app \
    && chown -R app:app /app
USER app

CMD ["python", "math.py"]
