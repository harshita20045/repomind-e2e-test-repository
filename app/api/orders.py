"""Order API routes."""

from fastapi import APIRouter, Depends, HTTPException, status

from app.models.order import Order, OrderCreate
from app.services.order_service import OrderService
from app.main import get_order_service

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate, service: OrderService = Depends(get_order_service)) -> Order:
    return service.create_order(payload)


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: int, service: OrderService = Depends(get_order_service)) -> Order:
    order = service.get_order(order_id)
    if order is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order
