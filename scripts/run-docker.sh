#!/bin/bash
# =============================================================================
# Run Application with Docker
# =============================================================================

set -e

echo "🐳 Building and running DevOps Demo App with Docker..."

# Navigate to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

# Configuration
IMAGE_NAME="devops-flask-app"
CONTAINER_NAME="flask-app-container"
PORT=5000

# Stop existing container if running
echo "🛑 Stopping existing container..."
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

# Build Docker image
echo "🔨 Building Docker image..."
docker build -t $IMAGE_NAME:latest -f docker/Dockerfile .

# Run container
echo "🚀 Starting container..."
docker run -d \
    --name $CONTAINER_NAME \
    --restart unless-stopped \
    -p $PORT:5000 \
    -e ENVIRONMENT=development \
    $IMAGE_NAME:latest

# Wait for container to start
echo "⏳ Waiting for container to start..."
sleep 5

# Health check
echo "🔍 Checking health..."
if curl --fail http://localhost:$PORT/health 2>/dev/null; then
    echo ""
    echo "✅ Application is running!"
    echo "🌐 Access at: http://localhost:$PORT"
else
    echo "❌ Health check failed!"
    docker logs $CONTAINER_NAME
    exit 1
fi
