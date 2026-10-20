import pytest
from pydantic import ValidationError

from pizzapilot.domain.models import MenuItem, Order, OrderLine, OrderStatus


def test_valid_menu_item():
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )

    assert pizza.name == "Margherita"
    assert pizza.price_minor_units == 25000
    assert pizza.size_options == ("Regular", "Large")


def test_empty_name_is_rejected():
    with pytest.raises(ValidationError):
        MenuItem(
            id="pizza-001",
            name="",
            size_options=("Regular",),
            price_minor_units=25000,
            available=True,
        )


def test_negative_price_is_rejected():
    with pytest.raises(ValidationError):
        MenuItem(
            id="pizza-001",
            name="Margherita",
            size_options=("Regular",),
            price_minor_units=-100,
            available=True,
        )


def test_empty_size_options_is_rejected():
    with pytest.raises(ValidationError):
        MenuItem(
            id="pizza-001",
            name="Margherita",
            size_options=(),
            price_minor_units=25000,
            available=True,
        )


def zero_price_is_accepted():
    pizza = MenuItem(
        id="pizza-002",
        name="Free Sample",
        size_options=("Regular",),
        price_minor_units=0,
        available=True,
    )

    assert pizza.price_minor_units == 0


def test_OrderLine_valid():
    order_line = OrderLine(menu_item_id="pizza-001", size="Regular", quantity=2)

    assert order_line.menu_item_id == "pizza-001"
    assert order_line.size == "Regular"
    assert order_line.quantity == 2


def test_zero_quantity_is_rejected():
    with pytest.raises(ValidationError):
        OrderLine(menu_item_id="pizza-001", size="Regular", quantity=0)


def test_valid_order():
    line = OrderLine(
        menu_item_id="pizza-001",
        size="Large",
        quantity=2,
    )

    order = Order(
        id="ORD-001",
        customer="Rahul",
        lines=(line,),
    )

    assert order.id == "ORD-001"
    assert order.status == OrderStatus.PENDING
    assert len(order.lines) == 1


def check_empty_lines_is_rejected():
    with pytest.raises(ValidationError):
        Order(
            id="ORD-002",
            customer="Rahul",
            lines=(),
        )


def check_empty_customer_is_rejected():
    with pytest.raises(ValidationError):
        Order(
            id="ORD-003",
            customer="",
            lines=(
                OrderLine(
                    menu_item_id="pizza-001",
                    size="Regular",
                    quantity=1,
                ),
            ),
        )


def check_empty_id_is_rejected():
    with pytest.raises(ValidationError):
        Order(
            id="",
            customer="Rahul",
            lines=(
                OrderLine(
                    menu_item_id="pizza-001",
                    size="Regular",
                    quantity=1,
                ),
            ),
        )


def check_menu_item_is_imutable():
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )

    with pytest.raises(TypeError):
        pizza.name = "Pepperoni"
