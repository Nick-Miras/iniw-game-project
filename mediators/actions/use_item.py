from custom_types import ID
from database import GetInventory, GetItem
from database.update import UpdateInventory
from datum.entity import Player
from datum.enumerations import MetadataType
from datum.items import ItemTypeMetadata


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


def use_item(player: Player, item_id: ID):
    inventory = GetInventory.execute(player.inventory_id)
    inventory.does_item_exist(item_id)

    item = GetItem.execute(item_id)
    if item.reusable is True:
        player.equipped_item = item
    else:
        player.items_applied.append(item)

    UpdateInventory.execute(inventory)


def clean_player_modifications(item_metadata: ItemTypeMetadata) -> bool:
    """
    Returns:
        True if the item should be removed from applied items; false if otherwise.
    """
    return item_metadata.item_type not in (MetadataType.DamageMultiplier, MetadataType.HealthMultiplier)


def apply_used_items(player: Player):
    for item_id in player.items_applied:
        item = GetItem.execute(item_id)
        apply_player_modifications(player, item.metadata)
        if clean_player_modifications(item.metadata) is True:
            player.items_applied.remove(item)
