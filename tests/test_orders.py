from fastapi.testclient import TestClient

from app.dependencies import order_repository, user_repository
from app.main import app

client = TestClient(app)


def setup_function() -> None:
    user_repository.clear()
    order_repository.clear()


def test_create_and_get_order() -> None:
    user = client.post("/users", json={"name": "Ada", "email": "ada@example.com"}).json()
    response = client.post("/orders", json={"user_id": user["id"], "items": [{"sku": "book", "quantity": 2, "unit_price": 10}]})
    assert response.status_code == 201
    assert response.json()["total"] == 22.0
    order_id = response.json()["id"]
    assert client.get(f"/orders/{order_id}").status_code == 200


def test_order_requires_existing_user() -> None:
    response = client.post("/orders", json={"user_id": 999, "items": [{"sku": "book", "quantity": 1, "unit_price": 10}]})
    assert response.status_code == 404


def test_missing_order() -> None:
    assert client.get("/orders/999").status_code == 404
