from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import TEST_DB_URL
from db.base import Base, get_db
from main import app


engine = create_engine(
    TEST_DB_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)
token = ''
product_id = ''


def test_create_user():
    response = client.post('/users', json={'name': 'foo',
                                           'email': 'foo@bar.com',
                                           'password': 'password',
                                           'password2': 'password'})

    assert response.status_code == 200


def test_read_users():
    response = client.get('/users')
    assert response.status_code == 200


def test_login():
    global token
    response = client.post('/login', json={'email': 'foo@bar.com',
                                           'password': 'password'})

    assert response.status_code == 200
    token = response.json()['access_string']
    print(token)


def test_create_product():
    global product_id
    response = client.post('/products', headers={'accept': 'application/json',
                                                 'Authorization': 'Bearer {}'.format(token)},
                           json={'name': 'name',
                                 'description': 'description'})

    assert response.status_code == 200
    product_id = response.json()['UUID']


def test_read_products():
    response = client.get('/products', headers={'accept': 'application/json',
                                                'Authorization': 'Bearer {}'.format(token)})
    assert response.status_code == 200


def test_delete_product():
    response = client.delete('products/{}'.format(product_id), headers={'accept': 'application/json',
                                                  'Authorization': 'Bearer {}'.format(token)})


def test_delete_user():
    response = client.delete('/users/{}'.format('1'), headers={'accept': 'application/json',
                                                               'Authorization': 'Bearer {}'.format(token)})
    assert response.status_code == 200



