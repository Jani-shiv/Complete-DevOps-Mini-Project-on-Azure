#!/bin/bash
# =============================================================================
# Run Application Locally (without Docker)
# =============================================================================

set -e

echo "🚀 Starting DevOps Demo App locally..."

# Navigate to project root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_ROOT"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Run setup.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Set environment variables
export FLASK_ENV=development
export FLASK_DEBUG=1
export ENVIRONMENT=development

# Run application
echo "📡 Starting Flask development server..."
echo "🌐 Access at: http://localhost:5000"
echo ""
cd src && python app.py
