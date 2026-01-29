"""
Application Tests
=================
Unit tests for the Flask application.
"""

import pytest


class TestHomePage:
    """Tests for the home page endpoint."""

    def test_home_returns_200(self, client):
        """Test that home page returns 200 status code."""
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_app_name(self, client):
        """Test that home page contains application name."""
        response = client.get("/")
        assert b"DevOps Demo App" in response.data

    def test_home_contains_tech_stack(self, client):
        """Test that home page shows tech stack badges."""
        response = client.get("/")
        assert b"Flask" in response.data
        assert b"Docker" in response.data
        assert b"Azure" in response.data


class TestAPIInfo:
    """Tests for the API info endpoint."""

    def test_api_info_returns_200(self, client):
        """Test that API info returns 200 status code."""
        response = client.get("/api/info")
        assert response.status_code == 200

    def test_api_info_returns_json(self, client):
        """Test that API info returns JSON content type."""
        response = client.get("/api/info")
        assert response.content_type == "application/json"

    def test_api_info_contains_required_fields(self, client):
        """Test that API info contains all required fields."""
        response = client.get("/api/info")
        data = response.get_json()

        assert "application" in data
        assert "version" in data
        assert "environment" in data
        assert "hostname" in data
        assert "endpoints" in data
        assert "tech_stack" in data

    def test_api_info_endpoints_list(self, client):
        """Test that endpoints are correctly listed."""
        response = client.get("/api/info")
        data = response.get_json()

        endpoints = data["endpoints"]
        assert endpoints["home"] == "/"
        assert endpoints["health"] == "/health"
        assert endpoints["info"] == "/api/info"


class TestErrorHandling:
    """Tests for error handling."""

    def test_404_returns_json(self, client):
        """Test that 404 errors return JSON."""
        response = client.get("/nonexistent-page")
        assert response.status_code == 404

        data = response.get_json()
        assert data["error"] == "Not Found"
        assert data["status_code"] == 404
