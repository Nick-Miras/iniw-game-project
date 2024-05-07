from pydantic import Field, BaseModel
from pydantic.dataclasses import dataclass
from enum import Enum, auto

from typing_extensions import Annotated


class MetadataType(Enum):  # TODO: Deliberate Whether To Use auto() or fill in manually
    HealthRestoration = auto()
    HealthMultiplier = auto()
    UltimateEnabler = auto()
    BaseDamage = auto()
    DamageMultiplier = auto()  # TODO: Possibly an ATTACK multiplier, not a DMG multiplier. Ask INIW
    AOEDamage = auto()  # by default, this is the damage multiplier for every other enemy
    UltimateDamageMultiplier = auto()
    UltimateAOEDamageMultiplier = auto()


class ItemTypeMetadata(BaseModel):
    item_type: MetadataType
    data: float | int

    class Config:
        use_enum_values = True


class Item(BaseModel):
    id: int
    name: str
    description: Annotated[str, Field(default=None)]
    price: int
    consumable: Annotated[bool, Field(default=False)]
    metadata: list[ItemTypeMetadata]


#########
# Weapons
#########


short_sword = Item(id=1, name='Short Sword', price=10, metadata=[
    ItemTypeMetadata(item_type=MetadataType.BaseDamage, data=50),
    ItemTypeMetadata(item_type=MetadataType.DamageMultiplier, data=1.2),
    ItemTypeMetadata(item_type=MetadataType.UltimateDamageMultiplier, data=3),  # not 300% but 3
])

long_sword = Item(id=2, name='Long Sword', price=50, metadata=[
    ItemTypeMetadata(item_type=MetadataType.BaseDamage, data=75),
    ItemTypeMetadata(item_type=MetadataType.DamageMultiplier, data=1),
    ItemTypeMetadata(item_type=MetadataType.AOEDamage, data=0.5),
    ItemTypeMetadata(item_type=MetadataType.UltimateAOEDamageMultiplier, data=2)
])

#########
# Potions
#########


small_health_potion = Item(id=3, name='Small Health Potion', price=5, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthRestoration, data=0.25)
])

medium_health_potion = Item(id=4, name='Medium Health Potion', price=10, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthRestoration, data=0.5)
])

large_health_potion = Item(id=5, name='Large Health Potion', price=20, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthRestoration, data=1)
])

ult_potion = Item(id=6, name='Ultimate Potion', price=50, metadata=[
    ItemTypeMetadata(item_type=MetadataType.UltimateEnabler, data=1)  # 1 means true
])

double_damage_potion = Item(id=7, name='Damage Double Potion', price=15, metadata=[
    ItemTypeMetadata(item_type=MetadataType.DamageMultiplier, data=2)
])

absorption_potion = Item(id=9, name='Absorption Potion', price=20, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthMultiplier, data=2)
])
