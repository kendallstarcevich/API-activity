import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_square(client):
    response = client.get('/square/3')
    assert response.status_code == 200
    assert response.json == {"Area": 9, "Shape": "Square"}

def test_echo(client):
    response = client.get('/echo?arg1=test&arg2=123')
    assert response.status_code == 200
    assert response.json == {"arg1": "test", "arg2": "123"}
