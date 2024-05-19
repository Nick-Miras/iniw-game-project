from pydantic import BaseModel

from custom_types import ID
import database


class InventoryItemProperties(BaseModel):
    id: ID  # we are only storing the item ids to conserve on storage and prevent redundancy
    amount: int


class Inventory(BaseModel):
    id: ID
    items: list[InventoryItemProperties]

    def add_item(self, item_id: int, amount: int) -> None:
        if self.does_item_exist(item_id) is True:
            raise ValueError('Item already exists!')
        self.items.append(InventoryItemProperties(id=item_id, amount=amount))

    def update_item_with_amount(self, item_id: int, amount: int) -> None:
        """
        Updates `InventoryItemProperties` that matches @param item_id with @param amount.
        This does not increment.
        """
        if self.does_item_exist(item_id) is False:
            raise ValueError('Item is not found in inventory!')
        item_properties = self.get_item_properties(item_id)
        updated_item_properties = item_properties.model_copy()
        updated_item_properties.amount = amount
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
        for item_properties in self.items:
            if item_properties.id == item_id:
                return item_properties
        raise ValueError('Item is not found in inventory!')

    def display_information_of_items(self):
        for item_info in self.items:
            if item_info.amount != 0:
                item = database.get_item(item_info.id)
                item.get_info()
                print(f"Item Amount: {item_info.amount}")
        print("========================================================================")
