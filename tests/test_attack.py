from datum.enumerations import AttackType
from datum.items import perform_player_calculation_with_metadata, short_sword


def test_perform_player_calculation_with_metadata():
    metadata = short_sword.metadata
    player_damage = 0
    player_damage = perform_player_calculation_with_metadata(metadata[0], player_damage, AttackType.BasicAttack)
    assert player_damage == metadata[0].data
