from pydantic import BaseModel


class InventoryItemProperties(BaseModel):
    id: int  # we are only storing the item ids to conserve on storage and prevent redundancy
    amount: int


class Inventory(BaseModel):
    id: int
    items: list[InventoryItemProperties]

    def add_item(self, item_id: int, amount: int):
        self.items.append(InventoryItemProperties(id=item_id, amount=amount))
