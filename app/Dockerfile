# =============================================================================
# DOCKERFILE FOR FLASK APPLICATION
# =============================================================================
# Purpose: Creates a lightweight, production-ready container for our Flask app
# Base Image: Python 3.11 slim (minimal Debian-based image)
# Server: Gunicorn (production WSGI server)
# =============================================================================

# Stage 1: Use Python slim image to reduce container size
# Why slim? Full Python image is ~900MB, slim is ~150MB
FROM python:3.11-slim

# Set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files (reduces image size)
# PYTHONUNBUFFERED: Ensures Python output is sent straight to terminal (no buffering)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory inside container
# All subsequent commands will run from /app
WORKDIR /app

# Install system dependencies
# --no-install-recommends: Don't install unnecessary packages (smaller image)
# rm -rf /var/lib/apt/lists/*: Clean up apt cache (smaller image)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user for security
# Running as root inside container is a security risk
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

# Copy requirements first (Docker layer caching optimization)
# If requirements.txt hasn't changed, Docker uses cached layer
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir: Don't cache pip packages (smaller image)
# --upgrade pip: Ensure we have latest pip for security
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Change ownership of app files to non-root user
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose port 5000
# This is documentation - actual port mapping happens in docker run
EXPOSE 5000

# Health check - Docker will check if container is healthy
# --interval: Check every 30 seconds
# --timeout: Wait 10 seconds for response
# --retries: Mark unhealthy after 3 failures
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:5000/health || exit 1

# Run application with Gunicorn (production WSGI server)
# Why Gunicorn?
# - Flask's built-in server is for development only
# - Gunicorn handles multiple workers, process management, graceful restarts
# --bind 0.0.0.0:5000: Listen on all interfaces
# --workers 2: Number of worker processes (2*CPU+1 is the formula, but 2 is fine for small VMs)
# --threads 4: Threads per worker
# --timeout 120: Worker timeout in seconds
# app:app - First 'app' is filename (app.py), second 'app' is Flask instance variable
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "4", "--timeout", "120", "app:app"]
