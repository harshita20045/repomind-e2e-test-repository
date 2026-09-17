"""Shared application dependencies."""

from collections.abc import Generator

from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository

user_repository = UserRepository()
order_repository = OrderRepository()


def get_user_repository() -> Generator[UserRepository, None, None]:
    yield user_repository


def get_order_repository() -> Generator[OrderRepository, None, None]:
    yield order_repository
