import database
from database.create import AddInventory, AddItem
from datum.inventory import InventoryItemProperties, Inventory
from datum.items import large_health_potion, small_health_potion, short_sword


def test_add_inventory():
    inventory = Inventory(id=1, items=[
        InventoryItemProperties(id=small_health_potion.id, amount=2),
        InventoryItemProperties(id=large_health_potion.id, amount=1)
    ])
    AddInventory.execute(inventory)


def test_add_item():
    item = short_sword
    AddItem.execute(item)


def test_get_item():
    item = database.get_item(3)
    print(item)
