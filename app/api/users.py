"""User API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_user_repository
from app.models.user import User, UserCreate
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(
    repository: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repository)


@router.post("", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, service: UserService = Depends(get_user_service)) -> User:
    return service.create_user(payload)


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, service: UserService = Depends(get_user_service)) -> User:
    user = service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
