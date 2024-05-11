from pydantic import BaseModel

from custom_types import ID
from datum.items import Item


class InventoryItemProperties(BaseModel):
    id: ID  # we are only storing the item ids to conserve on storage and prevent redundancy
    amount: int


class Inventory(BaseModel):
    id: ID
    items: list[InventoryItemProperties]

    def add_item(self, item_id: int, amount: int):
        if self.does_item_exist(item_id) is True:
            raise ValueError('Item already exists!')
        self.items.append(InventoryItemProperties(id=item_id, amount=amount))

    def update_item_with_amount(self, item_id: int, amount: int):
        if self.does_item_exist(item_id) is False:
            raise ValueError('Item is not found in inventory!')
        item_properties = self.get_item_properties(item_id)
        updated_item_properties = item_properties.model_copy()
        updated_item_properties.amount += amount
        self.items.remove(item_properties)
        self.items.append(InventoryItemProperties(id=item_id, amount=amount))

    def does_item_exist(self, item_id: int) -> bool:
        """
        Returns:
            True if item exists in inventory.
            False if item does not exist in inventory.
        """
        return any(item for item in self.items if item.id == item_id)

    def get_item_properties(self, item_id) -> InventoryItemProperties:
        return [item for item in self.items if item.id == item_id][0]
