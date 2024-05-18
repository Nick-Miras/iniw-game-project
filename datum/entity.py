from __future__ import annotations

from textwrap import dedent

from custom_types import ID
import database
from database.update import UpdateInventory
from datum.enumerations import AttackType
from generics.entity import (
    calculate_exp_gained_from_enemy_level,
    non_recursively_calculate_total_exp_at_level,
    calculate_level_from_total_exp,
    calculate_max_health_at_level,
    calculate_damage_at_level
)
from mediators.actions import attack, use_item

from pydantic import Field, BaseModel, field_validator
from typing import Any, TYPE_CHECKING, Optional
from typing_extensions import Annotated


class Entity(BaseModel):
    id: ID
    name: str
    maximum_health: int
    level: int
    current_health: Annotated[int, Field(default=0, init=False)]
    damage: Annotated[int, Field(default=0, init=False)]

    def model_post_init(self, __context: Any) -> None:
        self.current_health = self.maximum_health

    def get_info(self):
        """
        Display information about the mob's health.

        Returns:
            str: A message with current and maximum health.
        """
        return f"{self.name} - Current Level: {self.level} - Current Health: {self.current_health}/{self.maximum_health}"


class Mob(Entity):
    is_target_mob: Annotated[bool, Field(default=False)]


class Player(Entity):
    inventory_id: ID
    equipped_item: ID
    gold_balance: int
    experience: Annotated[Optional[float], Field(default=0, init=False)]
    maximum_health: Annotated[Optional[int], Field(default=0, init=False)]
    skill_points: Annotated[Optional[int], Field(default=0, init=False)]
    ultimate_points: Annotated[Optional[int], Field(default=0, init=False)]
    items_applied: Annotated[Optional[list[ID]], Field(default=[], init=False)]

    @field_validator('equipped_items', check_fields=False)
    @classmethod
    def items_must_exist(cls, v: list[ID]):
        for item in v:
            database.get_item(item)  # raises ValueError if item does not exist
        return v

    def get_info(self):

        return dedent(f"""\
        Player Name:{self.name}
        Current Level: {self.level}
        Current Health: {self.current_health}/{self.maximum_health}
        Weapon Equiped: {self.equipped_item}
        Gold Ballance: {self.gold_balance}
        Skill points{self.skill_points}/5
        Ult Points{self.ultimate_points}/3""")
    def current_info(self):
        return dedent(f"""\
        Current Health: {self.current_health}/{self.maximum_health}
        Skill points{self.skill_points}/5
        Ult Points{self.ultimate_points}/3""")
    def model_post_init(self, __context: Any) -> None:
        self.damage = calculate_damage_at_level(self.level)
        self.current_health = self.maximum_health = calculate_max_health_at_level(self.level)
        self.experience = non_recursively_calculate_total_exp_at_level(self.level)

    def attack(self, target_mobs: list[Mob], attack_type: AttackType):
        """
        Simulate an attack by this mob on another mob.

        Args:
            target_mobs: the target mob to attack
            attack_type: type of attack to execute

        Returns:
            str: a message describing the attack outcome
        """
        match attack_type:
            case AttackType.BasicAttack:
                self.skill_points += 1
                self.ultimate_points += 1
            case AttackType.SkillAttack:
                if self.skill_points < 1:
                    raise ValueError('You Do Not Have Enough Skill Points To Use A Skill!')
                self.ultimate_points += 2
                self.skill_points -= 1
            case AttackType.UltimateAttack:
                if self.ultimate_points < 3:
                    raise ValueError('You Do Not Have Enough Ultimate Points To Use An Ultimate Skill!')
                self.ultimate_points -= 3
        attack.attack(self, target_mobs, attack_type)
        if self.ultimate_points > 3:
            self.ultimate_points = 0
        if self.skill_points > 5:
            self.skill_points = 0

    def use_item(self, item_id: ID):
        use_item.use_item(self, item_id)
        use_item.apply_used_items(self)

    def level_up(self, enemy_level: int):
        self.experience += calculate_exp_gained_from_enemy_level(enemy_level)
        self.level = calculate_level_from_total_exp(self.experience)
        self.damage = calculate_damage_at_level(self.level)
        self.current_health = self.maximum_health = calculate_max_health_at_level(self.level)

    def sell(self, item_id: ID, amount: int):
        inventory = database.get_inventory(self.inventory_id)
        current_amount = inventory.get_item_properties(item_id).amount
        if amount > current_amount:
            raise ValueError("Item Amount To Sell Exceeds Inventory's Current Amount")

        inventory.update_item_with_amount(current_amount - amount)
        UpdateInventory.execute(inventory)
