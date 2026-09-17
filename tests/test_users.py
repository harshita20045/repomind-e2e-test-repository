from fastapi.testclient import TestClient

from app.dependencies import order_repository, user_repository
from app.main import app

client = TestClient(app)


def setup_function() -> None:
    user_repository.clear()
    order_repository.clear()


def test_create_and_get_user() -> None:
    created = client.post("/users", json={"name": "Ada", "email": "ada@example.com"})
    assert created.status_code == 201
    user_id = created.json()["id"]
    fetched = client.get(f"/users/{user_id}")
    assert fetched.status_code == 200
    assert fetched.json()["email"] == "ada@example.com"


def test_missing_user() -> None:
    assert client.get("/users/999").status_code == 404
