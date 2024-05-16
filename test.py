from app import app  
import pytest 

@pytest.fixture
def client():
  with app.test_client() as c:
    yield c

def test_Root(client):
  response = client.get('/')
  assert response.status_code == 302    
  assert response.location == '/register'    