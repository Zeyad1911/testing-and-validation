import pytest
from app import app  
from db import db

@pytest.fixture(scope="session")  
def database():
    conn = db.connectdb()  
    yield conn  
    conn.close() 

@pytest.fixture
def client(database):  
    with app.test_client() as client:
        with client.session_transaction():  
            db.create_table(database)  
        yield client

def test_root_redirects_to_register(client):
    response = client.get('/')
    assert response.status_code == 302
    assert response.location == '/register'

def test_successful_registration(client, database):
    # Simulate successful POST request
    data = {'name': 'John Doe', 'email': 'john.doe@example.com', 'password': 'secret123'}
    response = client.post('/register', data=data)

  
    assert response.status_code == 200
    assert 'passed_reg.html' in response.templates  #

    cursor = database.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ?", (data['email'],))
    user = cursor.fetchone()
    assert user is not None
    assert user['name'] == data['name']


def test_duplicate_email_registration(client, database):

    data = {'name': 'John Doe', 'email': 'john.doe@example.com', 'password': '12345'}
    client.post('/register', data=data)


    data = {'name': 'Jane Doe', 'email': 'john.doe@example.com', 'password': '12345'}
    response = client.post('/register', data=data)

    assert response.status_code in (400, 302)  

    

def test_missing_form_data(client):
    
    response = client.post('/register', data={})
    assert response.status_code in (400, 302)  
