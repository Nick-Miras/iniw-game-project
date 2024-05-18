from __future__ import annotations

from typing import TYPE_CHECKING

from custom_types import ID
from .read import GetItem, GetInventory, GetPlayer
from .delete import DeletePlayer, DeleteInventory
from .create import AddPlayer, AddInventory

if TYPE_CHECKING:
    from datum.entity import Player
    from datum.inventory import Inventory
    from datum.items import Item


def create_inventory(inventory: Inventory):
    AddInventory.execute(inventory)


def create_player(player: Player):
    AddPlayer.execute(player)


def get_item(item_id: ID) -> Item:
    return GetPlayer.execute(item_id)


def get_inventory(inventory_id: ID) -> Inventory:
    return GetInventory.execute(inventory_id)


def get_player(player_id: ID) -> Player:
    return GetPlayer.execute(player_id)


def delete_player(player: Player) -> None:
    DeletePlayer.execute(player)


def delete_inventory(inventory: Inventory) -> None:
    DeleteInventory.execute(inventory)
