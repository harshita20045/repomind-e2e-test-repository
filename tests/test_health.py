from fastapi.testclient import TestClient

from app.dependencies import order_repository, user_repository
from app.main import app

client = TestClient(app)


def setup_function() -> None:
    user_repository.clear()
    order_repository.clear()


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
