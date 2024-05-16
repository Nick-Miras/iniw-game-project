from database.create import AddInventory
from database.read import GetInventory, GetItem
from datum.entity import Player
from datum.items import small_health_potion, large_health_potion, short_sword, Item
from datum.inventory import InventoryItemProperties, Inventory
from mediators.shop import Shop
import pytest


def test_if_item_exists():
    GetItem.execute(1)
    GetItem.execute(3)
    with pytest.raises(ValueError):
        GetItem.execute(4)


def test_isinstance_item():
    assert isinstance(small_health_potion, Item) is True


def test_create_inventory():  # destructive
    inventory = Inventory(id=1, items=[
        InventoryItemProperties(id=small_health_potion.id, amount=1),
        InventoryItemProperties(id=large_health_potion.id, amount=1)
    ])
    print(inventory)
    AddInventory.execute(inventory)


def test_if_inventories_are_equal():
    inventory = Inventory(id=1, items=[
        InventoryItemProperties(id=small_health_potion.id, amount=1),
        InventoryItemProperties(id=large_health_potion.id, amount=1)
    ])
    assert GetInventory.execute(1) == inventory


def test_shop():
    shop_inventory = Inventory(id=69, items=[
        InventoryItemProperties(id=short_sword.id, amount=1)
    ])

    player = Player(
        name='iniw',
        damage=10,
        maximum_health=100,
        level=1,
        inventory_id=1,
        gold_balance=300,
        equipped_items=[small_health_potion.id]
    )
    shop = Shop(player, shop_inventory)
    shop.buy(1, 1)

    assert shop.shop_inventory == Inventory(id=69, items=[
        InventoryItemProperties(id=short_sword.id, amount=0)
    ])
    assert player == Player(
        name='iniw',
        damage=10,
        maximum_health=100,
        level=1,
        inventory_id=1,
        gold_balance=49,  # 300 - 251(cost of a short sword)
        equipped_items=[small_health_potion.id]
    )

    with pytest.raises(ValueError):
        shop.buy(1, 1)
