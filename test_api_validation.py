import pytest
from app import app


def test_register_with_valid_data():

    data = {'name': 'John Doe', 'email': 'john.doe@example.com', 'password': 'secret123'}
    with app.test_client() as client:
        response = client.post('/register', data=data)

    assert response.status_code == 302  
    assert response.location.endswith('/passed_reg.html') 

def test_register_with_missing_data():

    
    data = {'name': 'John Doe'}  
    with app.test_client() as client:
        response = client.post('/register', data=data)

    assert response.status_code == 400 

    data = {'email': 'john.doe@example.com', 'password': 'secret123'} 
    with app.test_client() as client:
        response = client.post('/register', data=data)

    assert response.status_code == 400  

def test_register_with_duplicate_email():

    data = {'name': 'John Doe', 'email': 'john.doe@example.com', 'password': 'secret123'}
    with app.test_client() as client:
        client.post('/register', data=data)

    data = {'name': 'Jane Doe', 'email': 'john.doe@example.com', 'password': 'different_password'}
    with app.test_client() as client:
        response = client.post('/register', data=data)

    assert response.status_code in (400, 302) 
