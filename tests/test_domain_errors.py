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
