from abc import ABC, abstractmethod

from datum.entity import Entity, Player, Mob


class Actions(ABC):
    @abstractmethod
    def execute(self):
        ...


class Attack(Actions):
    """
    Handles Attacks With Respect To Item/s Equipped
    """

    def __init__(self, player: Player, enemies: list[Mob]):
        self.player = player
        self.enemies = enemies

    @staticmethod
    def calculate_player_damage(player):
        base_damage = player.damage
        # TODO: Add damage calculation for single target and aoe

    def execute(self):
        player = self.player
        # TODO: What is the distinction between single target attack and AOE
        # TODO: How do you target a mob?
        target_mob, = [mob for mob in self.enemies if mob.is_target_mob is True]
        target_mob.current_health -= self.calculate_player_damage(player)
        if target_mob.current_health <= 0:
            target_mob.current_health = 0
        if target_mob.current_health <= 0:
            return f"{player.name} defeated {target_mob.name}!"
        else:
            return f"{player.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.current_health}"
