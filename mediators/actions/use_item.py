from __future__ import annotations
from typing import TYPE_CHECKING
from custom_types import ID
import database
from datum.enumerations import MetadataType
from datum.items import ItemTypeMetadata

if TYPE_CHECKING:
    from datum.entity import Player


def match_player_modifications(player: Player, item_metadata: ItemTypeMetadata):
    match item_metadata:
        case MetadataType.HealthRestoration:
            player.current_health *= item_metadata.data
        case MetadataType.UltimateEnabler:
            if item_metadata.data == 1:
                player.ultimate_points = 3
        case MetadataType.HealthMultiplier:
            player.maximum_health *= item_metadata.data
        case MetadataType.DamageMultiplier:
            player.damage *= item_metadata.data


def apply_player_modifications(player: Player, item_properties: list[ItemTypeMetadata]):
    for item_metadata in item_properties:
        match_player_modifications(player, item_metadata)


def use_item(player: Player, item_id: ID) -> None:
    inventory = database.get_inventory(player.inventory_id)
    inventory.does_item_exist(item_id)

    item = database.get_item(item_id)
    if item.reusable is True:
        player.equipped_item = item.id
    else:
        player.items_applied.append(item.id)
        inventory.update_item_with_amount(item_id, inventory.get_item_properties(item_id).amount - 1)
    database.update_inventory(inventory)


def clean_player_modifications(item_metadata: list[ItemTypeMetadata]) -> bool:
    """
    Returns:
        True if the item should be removed from applied items; false if otherwise.
    """
    for metadata in item_metadata:
        if metadata.item_type in (MetadataType.DamageMultiplier, MetadataType.HealthMultiplier):
            return True
    return False


def apply_used_items(player: Player):
    for item_id in player.items_applied:
        item = database.get_item(item_id)
        apply_player_modifications(player, item.metadata)
        if clean_player_modifications(item.metadata) is True:
            player.items_applied.remove(item)
