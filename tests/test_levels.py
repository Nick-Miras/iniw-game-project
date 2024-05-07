from generics.levels import *


print(recursively_calculate_total_exp_at_level(1))
print(recursively_calculate_total_exp_at_level(2))
print(recursively_calculate_total_exp_at_level(3))
print(recursively_calculate_total_exp_at_level(4))
print(recursively_calculate_total_exp_at_level(5))
print('\n')
print(non_recursively_calculate_total_exp_at_level(1))
print(non_recursively_calculate_total_exp_at_level(2))
print(non_recursively_calculate_total_exp_at_level(3))
print(non_recursively_calculate_total_exp_at_level(4))
print(non_recursively_calculate_total_exp_at_level(5))
print('\n')
print(recursively_calculate_total_exp_at_level(12))
print(recursively_calculate_total_exp_at_level(13))
print('\n')
calculate_level_from_total_exp(12.5)
calculate_level_from_total_exp(37.5)
calculate_level_from_total_exp(75)


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
