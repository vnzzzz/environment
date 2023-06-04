from fastapi.testclient import TestClient
import starlette.status

from app.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json() == {"message": "Hello World"}


def test_create_user():
    email: str = "test1@example.com"
    password: str = "test1"
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == starlette.status.HTTP_200_OK
    assert response.json()["email"] == email


def test_create_duplicate_user():
    email: str = "test1@example.com"
    password: str = "test1"
    response = client.post(
        "/users/",
        json={"email": email, "password": password},
    )
    assert response.status_code == starlette.status.HTTP_400_BAD_REQUEST
