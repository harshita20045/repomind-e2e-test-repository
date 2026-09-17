"""In-memory order repository."""

from app.models.order import Order, OrderCreate


class OrderRepository:
    """Stores orders in a process-local dictionary for this fixture."""

    def __init__(self) -> None:
        self._orders: dict[int, Order] = {}
        self._next_id = 1

    def create(self, payload: OrderCreate, subtotal: float, tax: float, total: float) -> Order:
        order = Order(
            id=self._next_id,
            **payload.model_dump(),
            subtotal=subtotal,
            tax=tax,
            total=total,
            created_at=_utc_now(),
        )
        self._orders[order.id] = order
        self._next_id += 1
        return order

    def get(self, order_id: int) -> Order | None:
        return self._orders.get(order_id)

    def clear(self) -> None:
        self._orders.clear()
        self._next_id = 1


def _utc_now():
    from datetime import UTC, datetime

    return datetime.now(UTC)
