import pytest

from pizzapilot.domain.errors import UnknownItem
from pizzapilot.domain.models import MenuItem
from pizzapilot.services.menu_service import MenuService


def test_get_item_returns_matching_item():
    menu_item = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )
    service =  MenuService((menu_item,))
    result = service.get_item("pizza-001")
    assert menu_item.id == "pizza-001"
    assert menu_item.name == "Margherita"
    assert result == menu_item

def test_get_item_normalizes_id_before_comparison():
    menu_item = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )
    service =  MenuService((menu_item,))
    result = service.get_item("  PIZZA-001  ")
    assert result == menu_item    
    
def test_item_is_available():
    menu_item = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )
    service =  MenuService((menu_item,))
    assert service.is_available("pizza-001", "Large") is True

def test_item_is_not_available():
    menu_item = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )
    service =  MenuService((menu_item,))
    assert service.is_available("pizza-001", "Small") is False
    
def test_list_available_returns_only_available_items():
    available_item = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )
    unavailable_item = MenuItem(
        id="pizza-002",
        name="Farmhouse",
        size_options=("Regular", "Large"),
        price_minor_units=30000,
        available=False,
    )
    service = MenuService((available_item, unavailable_item))

    assert service.list_available() == (available_item,)

def test_list_available_returns_empty_tuple_for_empty_menu():
    service = MenuService(())

    assert service.list_available() == ()        
                
def test_get_item_raises_unknown_item_for_missing_id():
    menu_item = MenuItem(
        id="pizza-001",
        name="Margherita",
        size_options=("Regular", "Large"),
        price_minor_units=25000,
        available=True,
    )
    service = MenuService((menu_item,))

    with pytest.raises(UnknownItem) as exc_info:
        service.get_item("pizza-999")

    assert exc_info.value.code == "UNKNOWN_ITEM"
    assert exc_info.value.message == "Menu item pizza-999 was not found"
    assert exc_info.value.context == {"item_id": "pizza-999"}