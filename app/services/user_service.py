"""User business operations."""

from app.models.user import User, UserCreate
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create_user(self, payload: UserCreate) -> User:
        return self.repository.create(payload)

    def get_user(self, user_id: int) -> User | None:
        return self.repository.get(user_id)
