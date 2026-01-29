# =============================================================================
# Makefile - Common Development Commands
# =============================================================================
# Usage: make <target>
# =============================================================================

.PHONY: help install run dev docker-build docker-run docker-stop test lint clean deploy

# Default target
help:
	@echo "╔═══════════════════════════════════════════════════════════════╗"
	@echo "║           DevOps Demo App - Available Commands                ║"
	@echo "╠═══════════════════════════════════════════════════════════════╣"
	@echo "║  make install      - Install dependencies                     ║"
	@echo "║  make run          - Run locally with Python                  ║"
	@echo "║  make dev          - Run with Docker Compose (hot-reload)     ║"
	@echo "║  make docker-build - Build Docker image                       ║"
	@echo "║  make docker-run   - Run Docker container                     ║"
	@echo "║  make docker-stop  - Stop Docker container                    ║"
	@echo "║  make test         - Run tests with pytest                    ║"
	@echo "║  make lint         - Lint code with flake8                    ║"
	@echo "║  make clean        - Clean up temporary files                 ║"
	@echo "╚═══════════════════════════════════════════════════════════════╝"

# =============================================================================
# Development
# =============================================================================

install:
	@echo "📦 Installing dependencies..."
	python -m pip install --upgrade pip
	pip install -r src/requirements.txt
	pip install pytest pytest-cov flake8 black
	@echo "✅ Dependencies installed"

run:
	@echo "🚀 Starting Flask development server..."
	cd src && python app.py

dev:
	@echo "🐳 Starting Docker Compose (development)..."
	docker-compose up --build

# =============================================================================
# Docker
# =============================================================================

docker-build:
	@echo "🔨 Building Docker image..."
	docker build -t devops-flask-app -f docker/Dockerfile .
	@echo "✅ Image built successfully"

docker-run: docker-stop
	@echo "🚀 Starting Docker container..."
	docker run -d \
		--name flask-app-container \
		-p 5000:5000 \
		-e ENVIRONMENT=development \
		devops-flask-app
	@echo "✅ Container started"
	@echo "🌐 Access at: http://localhost:5000"

docker-stop:
	@echo "🛑 Stopping container..."
	docker stop flask-app-container 2>/dev/null || true
	docker rm flask-app-container 2>/dev/null || true

docker-logs:
	docker logs -f flask-app-container

# =============================================================================
# Testing
# =============================================================================

test:
	@echo "🧪 Running tests..."
	pytest tests/ -v --cov=src --cov-report=term-missing

test-quick:
	@echo "🧪 Running quick tests..."
	pytest tests/ -v -x

lint:
	@echo "🔍 Linting code..."
	flake8 src/ --count --show-source --statistics
	@echo "✅ Linting complete"

format:
	@echo "✨ Formatting code with Black..."
	black src/ tests/
	@echo "✅ Formatting complete"

# =============================================================================
# Cleanup
# =============================================================================

clean:
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete"

clean-docker:
	@echo "🧹 Cleaning Docker resources..."
	docker system prune -f
	@echo "✅ Docker cleanup complete"

# =============================================================================
# Deployment
# =============================================================================

deploy:
	@echo "🚀 Triggering deployment..."
	git push origin main
	@echo "✅ Push complete - GitHub Actions will deploy"
