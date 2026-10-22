import pytest

from pizzapilot.domain.errors import (
    DomainError,
    EmptyOrder,
    InvalidQuantity,
    ItemUnavailable,
    UnknownItem,
)


@pytest.mark.parametrize(
    ("error_type", "expected_code", "message", "context"),
    [
        (
            UnknownItem,
            "UNKNOWN_ITEM",
            "Menu item was not found",
            {"item_id": "pizza-001"},
        ),
        (
            ItemUnavailable,
            "ITEM_UNAVAILABLE",
            "Menu item is unavailable",
            {"item_id": "pizza-001"},
        ),
        (
            InvalidQuantity,
            "INVALID_QUANTITY",
            "Quantity must be positive",
            {"quantity": 0},
        ),
        (
            EmptyOrder,
            "EMPTY_ORDER",
            "Order must contain at least one item",
            {},
        ),
    ],
)
def test_domain_error_subclasses(
    error_type: type[DomainError],
    expected_code: str,
    message: str,
    context: dict[str, object],
) -> None:
    error = error_type(message, context=context)

    assert isinstance(error, DomainError)
    assert error.code == expected_code
    assert error.message == message
    assert str(error) == message
    assert error.context == context


def menu_item_unavailable(item_id: str) -> None:
    raise ItemUnavailable(
        f"Menu item {item_id} is unavailable", context={"item_id": item_id}
    )


def find_item(item_id: str) -> None:
    raise UnknownItem(
        f"Menu item {item_id} was not found", context={"item_id": item_id}
    )


def normalize_id(item_id: str) -> None:
    if not item_id.isalnum():
        raise InvalidQuantity(
            f"Invalid item ID: {item_id}", context={"item_id": item_id}
        )
