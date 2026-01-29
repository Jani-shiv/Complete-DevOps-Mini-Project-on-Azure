"""
Health Endpoint Tests
=====================
Tests for the health check endpoint used by monitoring systems.
"""

import pytest


class TestHealthEndpoint:
    """Tests for the /health endpoint."""

    def test_health_returns_200(self, client):
        """Test that health endpoint returns 200 status code."""
        response = client.get("/health")
        assert response.status_code == 200

    def test_health_returns_json(self, client):
        """Test that health endpoint returns JSON content type."""
        response = client.get("/health")
        assert response.content_type == "application/json"

    def test_health_status_is_healthy(self, client):
        """Test that health status is 'healthy'."""
        response = client.get("/health")
        data = response.get_json()
        assert data["status"] == "healthy"

    def test_health_contains_timestamp(self, client):
        """Test that health response contains timestamp."""
        response = client.get("/health")
        data = response.get_json()
        assert "timestamp" in data
        # Verify ISO format
        assert "T" in data["timestamp"]

    def test_health_contains_hostname(self, client):
        """Test that health response contains hostname."""
        response = client.get("/health")
        data = response.get_json()
        assert "hostname" in data
        assert len(data["hostname"]) > 0

    def test_health_contains_version(self, client):
        """Test that health response contains version."""
        response = client.get("/health")
        data = response.get_json()
        assert "version" in data


class TestHealthEndpointPerformance:
    """Performance tests for health endpoint."""

    def test_health_response_time(self, client):
        """Test that health endpoint responds quickly."""
        import time

        start = time.time()
        response = client.get("/health")
        elapsed = time.time() - start

        assert response.status_code == 200
        # Health check should respond in under 100ms
        assert elapsed < 0.1

    def test_health_multiple_requests(self, client):
        """Test health endpoint handles multiple consecutive requests."""
        for _ in range(10):
            response = client.get("/health")
            assert response.status_code == 200
