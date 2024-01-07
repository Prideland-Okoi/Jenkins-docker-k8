import pytest
from flask import Flask

from app import app

@pytest.fixture
def client():
    # Create a test client using Flask's test_client
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    # Test the / endpoint
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Jenkins Docker Kubernetes Project!' in response.data
