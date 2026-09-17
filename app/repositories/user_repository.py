"""In-memory user repository."""

from app.models.user import User, UserCreate


class UserRepository:
    """Stores users in a process-local dictionary for this fixture."""

    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._next_id = 1

    def create(self, payload: UserCreate) -> User:
        user = User(id=self._next_id, **payload.model_dump(), created_at=_utc_now())
        self._users[user.id] = user
        self._next_id += 1
        return user

    def get(self, user_id: int) -> User | None:
        return self._users.get(user_id)

    def clear(self) -> None:
        self._users.clear()
        self._next_id = 1


def _utc_now():
    from datetime import UTC, datetime

    return datetime.now(UTC)
