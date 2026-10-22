from pizzapilot.domain.errors import UnknownItem
from pizzapilot.domain.models import MenuItem


class MenuService:
    def __init__(self, items: tuple[MenuItem, ...]) -> None:
        self._items = items
    
    
    def get_item(self, item_id: str) -> MenuItem:
        normalized_id = item_id.strip().casefold()

        for item in self._items:
            if item.id.strip().casefold() == normalized_id:
                return item

        raise UnknownItem(
            f"Menu item {item_id} was not found",
            context={"item_id": item_id},
        )
        
    def is_available(self, item_id: str, size: str) -> bool:
        item = self.get_item(item_id)
        if not item.available:
            return False

        return size in item.size_options
    
    def list_available(self) -> tuple[MenuItem, ...]:
        return tuple(item for item in self._items if item.available)
    