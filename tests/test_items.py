from datum.items import small_health_potion, large_health_potion, short_sword, Item
from datum.inventory import InventoryItemProperties, Inventory


def test_isinstance_item():
    assert isinstance(small_health_potion, Item) is True


def test_create_inventory():
    inventory = Inventory(id=1, items=[
        InventoryItemProperties(id=small_health_potion.id, amount=1),
        InventoryItemProperties(id=large_health_potion.id, amount=1)
    ])
    inventory.add_item(short_sword.id, 1)
    print(inventory)
    print(inventory.model_dump())
    print(short_sword.model_dump())
