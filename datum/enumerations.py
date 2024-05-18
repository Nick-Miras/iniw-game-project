from enum import Enum


class AttackType(Enum):
    BasicAttack = 'basic attack'
    SkillAttack = 'skill attack'
    UltimateAttack = 'ultimate attack'


class MetadataType(Enum):
    # potions
    HealthRestoration = 'health restoration'
    HealthMultiplier = 'health multiplier'
    UltimateEnabler = 'ultimate enabler'

    # weapons
    BaseDamage = 'base damage'
    DamageMultiplier = 'damage multiplier'
    UltimateDamageMultiplier = 'ultimate damage multiplier'
