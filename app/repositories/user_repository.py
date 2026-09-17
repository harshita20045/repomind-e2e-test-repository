from datetime import UTC, datetime
from app.models import User, UserCreate


class UserRepository:
    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._next_id = 1

    def create(self, payload: UserCreate) -> User:
        user = User(id=self._next_id, created_at=datetime.now(UTC), **payload.model_dump())
        self._users[user.id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> User | None:
        return self._users.get(user_id)
