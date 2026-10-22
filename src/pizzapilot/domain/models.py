from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class MenuItem(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    size_options: tuple[str, ...] = Field(min_length=1)
    price_minor_units: int = Field(ge=0)
    available: bool


class OrderLine(BaseModel):
    model_config = ConfigDict(frozen=True)

    menu_item_id: str = Field(min_length=1)
    size: str = Field(min_length=1)
    quantity: int = Field(gt=0)


class OrderStatus(StrEnum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Order(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str = Field(min_length=1)
    customer: str = Field(min_length=1)
    lines: tuple[OrderLine, ...] = Field(min_length=1)
    status: OrderStatus = OrderStatus.PENDING
