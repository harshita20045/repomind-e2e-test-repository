"""Order API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_order_repository, get_user_repository
from app.models.order import Order, OrderCreate
from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])


def get_order_service(
    orders: OrderRepository = Depends(get_order_repository),
    users: UserRepository = Depends(get_user_repository),
) -> OrderService:
    return OrderService(orders, users)


@router.post("", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate, service: OrderService = Depends(get_order_service)) -> Order:
    return service.create_order(payload)


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, service: OrderService = Depends(get_order_service)) -> Order:
    order = service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order
