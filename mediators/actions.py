from abc import ABC, abstractmethod

from database.read import GetItem
from datum.items import perform_player_calculation_with_metadata


class Actions(ABC):
    @classmethod
    @abstractmethod
    def execute(cls, player, enemies: list['Mob']):
        ...


class ShowInfo(Actions):
    pass


class UseItem(Actions):
    pass


class Attack(Actions):
    """
    Handles Attacks With Respect To Item/s Equipped
    """

    @staticmethod
    def calculate_player_damage(player) -> float:
        equipped_item = GetItem.execute(player.equipped_item)

        for metadata in equipped_item.metadata:
            perform_player_calculation_with_metadata(metadata, player)

        return player.damage

    @staticmethod
    def get_selected_mob(enemies: list['Mob']):
        for mob in enemies:
            if mob.is_target_mob is True:
                return mob

    @classmethod
    def execute(cls, player, enemies: list['Mob']):
        target_mob = cls.get_selected_mob(enemies)
        target_mob.current_health -= cls.calculate_player_damage(player)
        if target_mob.current_health <= 0:
            target_mob.current_health = 0
        if target_mob.current_health <= 0:
            return f"{player.name} defeated {target_mob.name}!"
        else:
            return f"{player.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.current_health}"
