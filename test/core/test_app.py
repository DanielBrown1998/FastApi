from http import HTTPStatus
from fastapi.testclient import TestClient
import sys

sys.path.append('c:/Users/Daniel/devs/FastApi')

from core.app import app


def test_root_would_return_hello_world():
    client = TestClient(app)
    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello, World"}
