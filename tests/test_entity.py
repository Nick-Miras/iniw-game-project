import database
from database.create import AddPlayer
from database.delete import DeletePlayer
from datum.entity import Entity, Player
from datum.items import stick
from generics.entity import recursively_calculate_total_exp_at_level, non_recursively_calculate_total_exp_at_level, \
    calculate_level_from_total_exp, calculate_exp_gained_from_enemy_level, calculate_max_health_at_level, \
    calculate_damage_at_level
from mediators.game import create_new_player


def test_entity(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Mark")
    player = create_new_player()
    print(player)
    player.level_up(10)
    print(player)


def test_calculate_required_exp_at_each_level():
    level = 1
    assert level * 40 == 40

    level = 2
    assert level * 40 == 80

    level = 3
    assert level * 40 == 120


def test_calculate_required_exp_at_each_level_2():
    assert recursively_calculate_total_exp_at_level(0) == 0
    assert recursively_calculate_total_exp_at_level(1) == 40
    assert recursively_calculate_total_exp_at_level(2) == 120
    assert recursively_calculate_total_exp_at_level(3) == 240


def test_calculate_total_exp_at_level():
    assert recursively_calculate_total_exp_at_level(0) == non_recursively_calculate_total_exp_at_level(0)
    assert recursively_calculate_total_exp_at_level(1) == non_recursively_calculate_total_exp_at_level(1)
    assert recursively_calculate_total_exp_at_level(3) == non_recursively_calculate_total_exp_at_level(3)
    assert recursively_calculate_total_exp_at_level(5) == non_recursively_calculate_total_exp_at_level(5)


def test_calculate_level_from_total_exp():
    assert calculate_level_from_total_exp(240) == 3


def test_calculate_level():
    exp_gained = calculate_exp_gained_from_enemy_level(10)


def test_calculate_max_health_at_level():
    assert calculate_max_health_at_level(0) == 0
    assert calculate_max_health_at_level(1) == 5
    assert calculate_max_health_at_level(2) == 10
    assert calculate_max_health_at_level(3) == 15


def test_calculate_damage_at_level():
    assert calculate_damage_at_level(0) == 0
    assert calculate_damage_at_level(1) == 2
    assert calculate_damage_at_level(2) == 4
    assert calculate_damage_at_level(3) == 6


def test_add_player():
    player_1 = Player(
        id=1,
        name='Iniw',
        level=1,
        inventory_id=1,
        gold_balance=300,
        equipped_item=stick.id
    )

    AddPlayer.execute(player_1)


def test_delete_player():
    player_1 = Player(
        id=1,
        name='Iniw',
        level=1,
        inventory_id=1,
        gold_balance=300,
        equipped_item=stick.id
    )

    database.delete_player(player_1.id)
