from textwrap import dedent
from typing import Optional

from pydantic import Field, BaseModel

from typing_extensions import Annotated

from custom_types import ID
from datum.enumerations import MetadataType


class ItemTypeMetadata(BaseModel):
    item_type: MetadataType
    data: float | int

    class Config:
        use_enum_values = True


class Item(BaseModel):
    id: ID
    name: str
    description: Annotated[Optional[str], Field(default='')]
    price: int
    consumable: Annotated[Optional[bool], Field(default=False)]
    reusable: Annotated[Optional[bool], Field(default=False)]
    metadata: list[ItemTypeMetadata]

    def get_info(self):
        stats = '\n'.join(f"{metadatum.item_type.title()}: {metadatum.data}" for metadatum in self.metadata)
        info = dedent(f"""\
        ========================================================================
        Item ID: {self.id}
        Item Name: {self.name}
        Item Description: {self.description}
        Item Price: {self.price}
        Item Stats:""")
        print(info)
        print(stats)


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

##############################
# Duration Of Enemy Engagement
##############################

double_damage_potion = Item(id=7, name='Damage Double Potion', price=25, metadata=[
    ItemTypeMetadata(item_type=MetadataType.DamageMultiplier, data=2)
])

absorption_potion = Item(id=9, name='Absorption Potion', price=20, metadata=[
    ItemTypeMetadata(item_type=MetadataType.HealthMultiplier, data=2)
])

game_items = [
    short_sword,
    stick,
    small_health_potion,
    medium_health_potion,
    large_health_potion,
    ult_potion,
    absorption_potion,
    double_damage_potion
]
