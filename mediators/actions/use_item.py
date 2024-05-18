from custom_types import ID
from database import GetInventory
from datum.entity import Player


def use_item(player: Player, item: ID):
    inventory = GetInventory.execute(player.inventory_id)
