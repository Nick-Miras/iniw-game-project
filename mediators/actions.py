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

    def calculate_player_damage(self):
        base_damage = self.player.damage


    def execute(self):
        player = self.player
        target_mob, = [mob for mob in self.enemies if mob.is_target_mob is True]
        target_mob.current_health -= player.damage
        if target_mob.current_health <= 0:
            target_mob.current_health = 0
        if target_mob.current_health <= 0:
            return f"{self.name} defeated {target_mob.name}!"
        else:
            return f"{self.name} attacked {target_mob.name}. {target_mob.name}'s health: {target_mob.current_health}"