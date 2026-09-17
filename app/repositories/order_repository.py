from datetime import UTC, datetime
from app.models import Order, OrderCreate


class OrderRepository:
    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def create(self, payload: OrderCreate, subtotal: float, total: float) -> Order:
        order = Order(id=self._next_id, created_at=datetime.now(UTC), subtotal=subtotal, total=total, **payload.model_dump())
        self._orders[order.id] = order
        self._next_id += 1
        return order

    def get(self, order_id: int) -> Order | None:
        return self._orders.get(order_id)
