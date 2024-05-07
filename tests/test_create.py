import json
from json import JSONDecodeError

from database.create import Create, AddInventory
from datum.inventory import InventoryItemProperties, Inventory
from datum.items import large_health_potion, small_health_potion


def test_add_inventory():
    inventory = Inventory(id=1, items=[
        InventoryItemProperties(id=small_health_potion.id, amount=2),
        InventoryItemProperties(id=large_health_potion.id, amount=1)
    ])
    AddInventory.execute(inventory)
