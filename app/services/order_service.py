"""Order business operations, including ownership and total calculation."""

from fastapi import HTTPException, status

from app.config import settings
from app.models.order import Order, OrderCreate
from app.repositories.order_repository import OrderRepository
from app.repositories.user_repository import UserRepository


class OrderService:
    def __init__(self, orders: OrderRepository, users: UserRepository) -> None:
        self.orders = orders
        self.users = users

    def create_order(self, payload: OrderCreate) -> Order:
        if self.users.get(payload.user_id) is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        subtotal = round(sum(item.quantity * item.unit_price for item in payload.items), 2)
        tax = round(subtotal * settings.order_tax_rate, 2)
        total = round(subtotal + tax, 2)
        return self.orders.create(payload, subtotal, tax, total)

    def get_order(self, order_id: int) -> Order | None:
        return self.orders.get(order_id)
