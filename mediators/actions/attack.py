from datum.enumerations import AttackType
from database import GetItem
from datum.items import perform_player_calculation_with_metadata


def calculate_player_damage(player, attack_type: AttackType) -> float:
    equipped_item = GetItem.execute(player.equipped_item)

    player_damage = player.damage
    for metadata in equipped_item.metadata:
        player_damage = perform_player_calculation_with_metadata(metadata, player_damage, attack_type)

    return player_damage


def get_selected_mob(enemies: list['Mob']):
    for mob in enemies:
        if mob.is_target_mob is True:
            return mob


def attack(player, enemies: list['Mob'], attack_type: AttackType):
    target_mob = get_selected_mob(enemies)
    target_mob.current_health -= calculate_player_damage(player, attack_type)
    if target_mob.current_health <= 0:
        target_mob.current_health = 0
    if target_mob.current_health <= 0:
        return f"{player.name} defeated {target_mob.name}!"
    else:
        return f"{player.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.current_health}"