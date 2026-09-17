"""FastAPI application entry point."""

from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.users import router as users_router
from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository
from app.services.order_service import OrderService
from app.services.user_service import UserService

user_repository = UserRepository()
order_repository = OrderRepository()


def get_user_service() -> UserService:
    return UserService(user_repository)


def get_order_service() -> OrderService:
    return OrderService(order_repository, user_repository)


app = FastAPI(title="RepoMind Fixture API")
app.include_router(health_router)
app.include_router(users_router)

# Imported after service dependencies are defined to avoid circular imports.
from app.api.orders import router as orders_router  # noqa: E402

app.include_router(orders_router)
