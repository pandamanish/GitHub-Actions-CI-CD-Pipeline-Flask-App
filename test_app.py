# test_app.py
import pytest
from app import app  # Import the Flask app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client  # This will be the test client

def test_hello(client):
    response = client.get('/')
    assert response.data == b"Hello, World!"
    assert response.status_code == 200

def test_add(client):
    response = client.get('/add/2/3')
    assert response.data == b"5"
    assert response.status_code == 200

def test_add_invalid(client):
    response = client.get('/add/2/a')
    assert response.status_code == 404  # Check for a 404 error
