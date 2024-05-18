import database
from database import get_inventory
from datum.entity import Player
from datum.inventory import Inventory, InventoryItemProperties
from datum.items import (
    short_sword, 
    small_health_potion, 
    medium_health_potion, 
    large_health_potion, 
    ult_potion, 
    double_damage_potion, 
    absorption_potion
)


class Shop:
    def __init__(self, player: Player, shop_inventory: Inventory):
        self.player = player
        self.shop_inventory = shop_inventory  # TODO: could be just inventory id

    def _validate_for_available_stock(self, item_id: int, amount_requested: int):
        if (self.shop_inventory.get_item_properties(item_id).amount < amount_requested) is True:
            raise ValueError(f'There Is Not Enough Stock Of Item: {item_id}!')

    def _validate_for_purchasing_capability(self, item_id: int):
        if (item_price := database.get_item(item_id).price) > (balance := self.player.gold_balance) is True:
            raise ValueError(f'Player Does Not Have Enough Balance! Item Price: {item_price} > {balance}')

    def _is_item_in_inventory(self, item_id: int) -> bool:
        return self.shop_inventory.does_item_exist(item_id)

    def buy(self, item_id: int, amount: int) -> Player:
        if self._is_item_in_inventory(item_id) is False:
            raise ValueError('Item Is Not In Shop Inventory.')

        self._validate_for_available_stock(item_id, amount)
        self._validate_for_purchasing_capability(item_id)

        player_inventory: Inventory = get_inventory(self.player.inventory_id)
        if player_inventory.does_item_exist(item_id) is True:
            current_amount = player_inventory.get_item_properties(item_id).amount
            player_inventory.update_item_with_amount(item_id, current_amount + amount)
        else:
            player_inventory.add_item(item_id, amount)
        self.player.gold_balance -= database.get_item(item_id).price
        self.shop_inventory.update_item_with_amount(
            item_id, self.shop_inventory.get_item_properties(item_id).amount - amount
        )
        return self.player


shop_inventory = Inventory(
    id=400,
    items=[
        InventoryItemProperties(id=short_sword.id, amount=1),
        InventoryItemProperties(id=small_health_potion.id, amount=99),
        InventoryItemProperties(id=medium_health_potion.id, amount=99),
        InventoryItemProperties(id=large_health_potion.id, amount=99),
        InventoryItemProperties(id=ult_potion.id, amount=99),
        InventoryItemProperties(id=double_damage_potion.id, amount=99),
        InventoryItemProperties(id=absorption_potion.id, amount=99),
    ]
)
