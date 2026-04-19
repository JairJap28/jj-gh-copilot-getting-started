import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """Provides a TestClient instance for all tests"""
    return TestClient(app)
