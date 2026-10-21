class DomainError(Exception):
    """Base class for expected business-domain failures."""

    code: str

    def __init__(
        self,
        message: str,
        *,
        context: dict[str, object] | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self.context = context or {}


class ValidationError(DomainError):
    """Raised when a business rule validation fails."""

    code = "validation_error"


class NotFoundError(DomainError):
    """Raised when a requested resource is not found."""

    code = "not_found_error"


class ConflictError(DomainError):
    """Raised when a business rule conflict occurs."""

    code = "conflict_error"


class ItemUnavailable(DomainError):
    """Raised when an Item Unavailable action is attempted."""

    code = "ITEM_UNAVAILABLE"


class OrderNotInProgress(DomainError):
    """Raised when an Order Not In Progress action is attempted."""

    code = "ORDER_NOT_IN_PROGRESS"


class UnknownItem(DomainError):
    """Raised when a requested menu item does not exist."""

    code = "UNKNOWN_ITEM"


class InvalidQuantity(DomainError):
    """Raised when an order quantity is invalid."""

    code = "INVALID_QUANTITY"


class EmptyOrder(DomainError):
    """Raised when an order contains no items."""

    code = "EMPTY_ORDER"
