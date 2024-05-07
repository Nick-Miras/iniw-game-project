from pydantic import Field
from pydantic.dataclasses import dataclass
from enum import Enum, auto

from typing_extensions import Annotated


class MetadataType(Enum):
    HealthRestoration = auto()
    HealthMultiplier = auto()
    UltimateEnabler = auto()
    BaseDamage = auto()
    DamageMultiplier = auto()  # TODO: Possible an ATTACK multiplier, not a DMG multiplier
    AOEDamage = auto()  # by default, this is the damage multiplier for every other enemy
    UltimateDamageMultiplier = auto()
    UltimateAOEDamageMultiplier = auto()
    DamageDebuffToEnemy = auto()


@dataclass
class ItemTypeMetadata:
    item_type: MetadataType
    data: float | int


@dataclass
class Item:
    id: int
    name: str
    description: Annotated[str, Field(default=None)]
    price: int
    consumable: Annotated[bool, Field(default=False)]
    metadata: list[ItemTypeMetadata]


@dataclass
class Inventory:
    id: int
    items: list[Item]

#########
# Weapons
#########


short_sword = Item(id=1, name='Short Sword', price=10, metadata=[
    ItemTypeMetadata(MetadataType.BaseDamage, 50),
    ItemTypeMetadata(MetadataType.DamageMultiplier, 1.2),
    ItemTypeMetadata(MetadataType.UltimateDamageMultiplier, 3),  # not 300% but 3
    ItemTypeMetadata(MetadataType.DamageDebuffToEnemy, 0.1)  # should lower enemy health by 10%
])

long_sword = Item(id=2, name='Long Sword', price=50, metadata=[
    ItemTypeMetadata(MetadataType.BaseDamage, 75),
    ItemTypeMetadata(MetadataType.DamageMultiplier, 1),
    ItemTypeMetadata(MetadataType.AOEDamage, 0.5),
    ItemTypeMetadata(MetadataType.UltimateAOEDamageMultiplier, 2)
])

#########
# Potions
#########


small_health_potion = Item(id=3, name='Small Health Potion', price=5, metadata=[
    ItemTypeMetadata(MetadataType.HealthRestoration, 0.25)
])

medium_health_potion = Item(id=4, name='Medium Health Potion', price=10, metadata=[
    ItemTypeMetadata(MetadataType.HealthRestoration, 0.5)
])

large_health_potion = Item(id=5, name='Large Health Potion', price=20, metadata=[
    ItemTypeMetadata(MetadataType.HealthRestoration, 1)
])

ult_potion = Item(id=6, name='Ultimate Potion', price=50, metadata=[
    ItemTypeMetadata(MetadataType.UltimateEnabler, 1)  # 1 means true
])

double_damage_potion = Item(id=7, name='Damage Double Potion', price=15, metadata=[
    ItemTypeMetadata(MetadataType.DamageMultiplier, 2)
])

absorption_potion = Item(id=9, name='Absorption Potion', price=20, metadata=[
    ItemTypeMetadata(MetadataType.HealthMultiplier, 2)
])
