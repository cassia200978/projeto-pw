from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_root_deve_retornar_ola_mundo():
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}