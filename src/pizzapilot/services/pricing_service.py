from pizzapilot.domain.errors import EmptyOrder, ItemUnavailable
from pizzapilot.domain.models import OrderLine, PricingResult
from pizzapilot.services.menu_service import MenuService


class PricingService:
    def __init__(self, menu_service: MenuService) -> None:
        self._menu_service = menu_service

    def price_order(self, order_lines: tuple[OrderLine, ...]) -> PricingResult:
        if not order_lines:
            raise EmptyOrder("Order must contain at least one item")
        subtotal = 0

        for line in order_lines:
            item = self._menu_service.get_item(line.menu_item_id)
            if not self._menu_service.is_available(line.menu_item_id, line.size):
                raise ItemUnavailable(
                    f"Item {line.menu_item_id} is unavailable for size {line.size}"
                )
            line_total = item.price_minor_units * line.quantity
            subtotal += line_total
        if subtotal >= 100_000:
            discount = (subtotal * 10 + 50) // 100
        else:
            discount = 0
        tax = ((subtotal - discount) * 5 + 50) // 100
        total = subtotal - discount + tax

        return PricingResult(
            subtotal_minor_units=subtotal,
            discount_minor_units=discount,
            tax_minor_units=int(tax),
            total_minor_units=int(total),
        )
