from pydantic import Field, BaseModel
from enum import Enum

from typing_extensions import Annotated

from custom_types import ID


class MetadataType(Enum):  # TODO: Deliberate Whether To Use auto() or fill in manually
    HealthRestoration = 'health restoration'
    HealthMultiplier = 'health multiplier'
    UltimateEnabler = 'ultimate enabler'
    BaseDamage = 'base damage'
    DamageMultiplier = 'damage multiplier'  # TODO: Possibly an ATTACK multiplier, not a DMG multiplier. Ask INIW
    UltimateDamageMultiplier = 'ultimate damage multiplier'


class ItemTypeMetadata(BaseModel):
    item_type: MetadataType
    data: float | int

    class Config:
        use_enum_values = True


class Item(BaseModel):
    id: ID
    name: str
    description: Annotated[str, Field(default='')]
    price: int
    consumable: Annotated[bool, Field(default=False)]
    reusable: Annotated[bool, Field(default=False)]
    metadata: list[ItemTypeMetadata]


def perform_player_calculation_with_metadata(metadata: ItemTypeMetadata, player: 'Player'):
    match metadata.item_type:
        case MetadataType.BaseDamage.value:
            player.damage += metadata.data
        case MetadataType.DamageMultiplier.value:
            player.damage *= metadata.data
    return player

#########
# Weapons
#########


short_sword = Item(id=1, name='Short Sword', price=100, reusable=True, metadata=[
    ItemTypeMetadata(item_type=MetadataType.BaseDamage, data=50),
    ItemTypeMetadata(item_type=MetadataType.DamageMultiplier, data=1.2),
    ItemTypeMetadata(item_type=MetadataType.UltimateDamageMultiplier, data=3),  # not 300% but 3
])

stick = Item(id=2, name='Stick', price=0, reusable=True, metadata=[
    ItemTypeMetadata(item_type=MetadataType.BaseDamage, data=10)
])

#########
# Potions
#########


small_health_potion = Item(id=3, name='Small Health Potion', price=10, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthRestoration, data=0.25)
])

medium_health_potion = Item(id=4, name='Medium Health Potion', price=25, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthRestoration, data=0.5)
])

large_health_potion = Item(id=5, name='Large Health Potion', price=50, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthRestoration, data=1)
])

ult_potion = Item(id=6, name='Ultimate Potion', price=75, metadata=[
    ItemTypeMetadata(item_type=MetadataType.UltimateEnabler, data=1)  # 1 means true
])

double_damage_potion = Item(id=7, name='Damage Double Potion', price=25, metadata=[
    ItemTypeMetadata(item_type=MetadataType.DamageMultiplier, data=2)
])

absorption_potion = Item(id=9, name='Absorption Potion', price=20, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthMultiplier, data=2)
])
