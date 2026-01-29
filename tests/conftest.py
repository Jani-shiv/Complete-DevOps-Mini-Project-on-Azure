"""
Pytest Configuration and Fixtures
=================================
Shared fixtures and configuration for all tests.
"""

import pytest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app as flask_app


@pytest.fixture
def app():
    """Create application for testing."""
    flask_app.config.update(
        {
            "TESTING": True,
            "DEBUG": True,
        }
    )
    yield flask_app


@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner."""
    return app.test_cli_runner()
