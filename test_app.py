import pytest
from app import app

# Set up a fixture for the test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    # Test the '/' route
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello, Duniya!'

def test_add_route(client):
    # Test the '/add/<int:a>/<int:b>' route
    response = client.get('/add/3/5')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '8'

    response = client.get('/add/10/20')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '30'
