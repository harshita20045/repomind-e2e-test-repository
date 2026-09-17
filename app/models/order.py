"""Order request and response models."""

from datetime import datetime
from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    sku: str = Field(min_length=1, max_length=100)
    quantity: int = Field(gt=0)
    unit_price: float = Field(gt=0)


class OrderCreate(BaseModel):
    user_id: int = Field(gt=0)
    items: list[OrderItem] = Field(min_length=1)


class Order(BaseModel):
    id: int
    user_id: int
    items: list[OrderItem]
    subtotal: float
    tax: float
    total: float
    created_at: datetime
