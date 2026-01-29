"""
Flask Web Application for DevOps Demo Project
==============================================
Author: DevOps Engineer
Purpose: Web application demonstrating CI/CD pipeline with Docker deployment on Azure

Endpoints:
    - GET /        : Home page with server information
    - GET /health  : Health check endpoint for monitoring
    - GET /api/info: API endpoint returning application details
"""

import os
import socket
from datetime import datetime

from flask import Flask, jsonify, render_template
from config import get_config

# Initialize Flask application
app = Flask(__name__)

# Load configuration
config = get_config()
app.config.from_object(config)


@app.route("/")
def home():
    """
    Main page showing server information and deployment status.

    Returns:
        Rendered HTML template with server details.
    """
    return render_template(
        "index.html",
        app_name=config.APP_NAME,
        hostname=socket.gethostname(),
        server_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment=config.ENVIRONMENT,
        version=config.APP_VERSION,
    )


@app.route("/health")
def health():
    """
    Health check endpoint for monitoring and load balancers.

    Returns:
        JSON response with health status (200 OK if healthy).
    """
    return (
        jsonify(
            {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "hostname": socket.gethostname(),
                "version": config.APP_VERSION,
            }
        ),
        200,
    )


@app.route("/api/info")
def api_info():
    """
    API endpoint returning server and application information.

    Returns:
        JSON response with detailed application information.
    """
    return jsonify(
        {
            "application": config.APP_NAME,
            "version": config.APP_VERSION,
            "environment": config.ENVIRONMENT,
            "hostname": socket.gethostname(),
            "server_time": datetime.now().isoformat(),
            "endpoints": {"home": "/", "health": "/health", "info": "/api/info"},
            "tech_stack": {
                "framework": "Flask",
                "language": "Python 3.11",
                "container": "Docker",
                "ci_cd": "GitHub Actions",
                "cloud": "Azure VM",
            },
        }
    )


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return (
        jsonify(
            {
                "error": "Not Found",
                "message": "The requested resource was not found.",
                "status_code": 404,
            }
        ),
        404,
    )


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return (
        jsonify(
            {
                "error": "Internal Server Error",
                "message": "An unexpected error occurred.",
                "status_code": 500,
            }
        ),
        500,
    )


if __name__ == "__main__":
    # Run the application
    # In production, this will be behind Gunicorn
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)
