from abc import ABC, abstractmethod
from datum.inventory import Inventory
from datum.items import short_sword, MetadataType


class Actions(ABC):
    @classmethod
    @abstractmethod
    def execute(cls, player, enemies: list['Mob']):
        ...


class Attack(Actions):
    """
    Handles Attacks With Respect To Item/s Equipped
    """

    def __init__(self, player: 'Player', enemies: list['Mob']):
        self.player = player
        self.enemies = enemies

    @staticmethod
    def calculate_player_damage(player) -> float:
        player_damage = player.damage
        equipped_weapon = short_sword

        for metadatum in equipped_weapon.metadata:
            if metadatum.item_type == MetadataType.BaseDamage.value:
                player_damage += metadatum.data
            if metadatum.item_type == MetadataType.DamageMultiplier.value:
                player_damage *= metadatum.data

        return player_damage

    @classmethod
    def execute(cls, player, enemies: list['Mob']):
        # TODO: What is the distinction between single target attack and AOE
        # TODO: How do you target a mob?
        selected_mob = [mob for mob in enemies if mob.is_target_mob is True]
        target_mob = selected_mob[0]
        target_mob.current_health -= cls.calculate_player_damage(player)
        if target_mob.current_health <= 0:
            target_mob.current_health = 0
        if target_mob.current_health <= 0:
            return f"{player.name} defeated {target_mob.name}!"
        else:
            return f"{player.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.current_health}"
