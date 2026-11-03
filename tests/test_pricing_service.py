import pytest

from pizzapilot.domain.errors import EmptyOrder, ItemUnavailable, UnknownItem
from pizzapilot.domain.models import MenuItem, OrderLine
from pizzapilot.services.menu_service import MenuService
from pizzapilot.services.pricing_service import PricingService


def test_price_order_without_discount() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=50_000,
        available=True,
    )
    menu_service = MenuService((pizza,))
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="pizza-001",
        size="Regular",
        quantity=1,
    )

    result = pricing_service.price_order((line,))

    assert result.subtotal_minor_units == 50_000
    assert result.discount_minor_units == 0
    assert result.tax_minor_units == 2_500
    assert result.total_minor_units == 52_500


def test_calculate_total_with_rounding() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=10,
        available=True,
    )
    menu_service = MenuService((pizza,))
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="pizza-001",
        size="Regular",
        quantity=1,
    )

    result = pricing_service.price_order((line,))

    assert result.subtotal_minor_units == 10
    assert result.discount_minor_units == 0
    assert result.tax_minor_units == 1
    assert result.total_minor_units == 11


def test_no_discount_applied() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=99_999,
        available=True,
    )
    menu_service = MenuService((pizza,))
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="pizza-001",
        size="Regular",
        quantity=1,
    )

    result = pricing_service.price_order((line,))

    assert result.subtotal_minor_units == 99_999
    assert result.discount_minor_units == 0
    assert result.tax_minor_units == 5_000
    assert result.total_minor_units == 104_999


def test_discount_applied_at_exact_threshold() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=100_000,
        available=True,
    )
    menu_service = MenuService((pizza,))
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="pizza-001",
        size="Regular",
        quantity=1,
    )

    result = pricing_service.price_order((line,))

    assert result.subtotal_minor_units == 100_000
    assert result.discount_minor_units == 10_000
    assert result.tax_minor_units == 4_500
    assert result.total_minor_units == 94_500


def test_empty_order_raises_error() -> None:
    menu_service = MenuService(())
    pricing_service = PricingService(menu_service)

    with pytest.raises(EmptyOrder) as exc_info:
        pricing_service.price_order(())

    assert exc_info.value.code == "EMPTY_ORDER"
    assert exc_info.value.message == "Order must contain at least one item"
    assert exc_info.value.context == {}


def test_unknown_menu_item_raises_error() -> None:
    menu_service = MenuService(())
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="unknown-item",
        size="Regular",
        quantity=1,
    )

    with pytest.raises(UnknownItem):
        pricing_service.price_order((line,))


def test_price_order_multiple_lines_and_quantities() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=50_000,
        available=True,
    )
    soda = MenuItem(
        id="soda-001",
        name="Cola",
        size_options=("Can",),
        price_minor_units=5_000,
        available=True,
    )
    menu_service = MenuService((pizza, soda))
    pricing_service = PricingService(menu_service)

    lines = (
        OrderLine(menu_item_id="pizza-001", size="Regular", quantity=2),
        OrderLine(menu_item_id="soda-001", size="Can", quantity=3),
    )

    result = pricing_service.price_order(lines)

    assert result.subtotal_minor_units == 115_000
    assert result.discount_minor_units == 11_500
    assert result.tax_minor_units == 5_175
    assert result.total_minor_units == 108_675


def test_unavailable_item_raises_error() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=50_000,
        available=False,
    )
    menu_service = MenuService((pizza,))
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="pizza-001",
        size="Regular",
        quantity=1,
    )

    with pytest.raises(ItemUnavailable):
        pricing_service.price_order((line,))


def test_unsupported_size_raises_error() -> None:
    pizza = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular",),
        price_minor_units=50_000,
        available=True,
    )
    menu_service = MenuService((pizza,))
    pricing_service = PricingService(menu_service)

    line = OrderLine(
        menu_item_id="pizza-001",
        size="Large",  # Unsupported size
        quantity=1,
    )

    with pytest.raises(ItemUnavailable):
        pricing_service.price_order((line,))
