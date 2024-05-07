from math import floor, sqrt


COMMON_DIFFERENCE_PER_LEVEL = 125


def calculate_exp_gained_from_enemy_level(enemy_level: int) -> int:
    return enemy_level * 10 + 25


def calculate_total_exp_after_exp_gain(current_experience: int, enemy_level: int) -> int:
    return current_experience + calculate_exp_gained_from_enemy_level(enemy_level)


def calculate_required_exp_for_level(level: int) -> int:
    return int(COMMON_DIFFERENCE_PER_LEVEL * level)


def recursively_calculate_total_exp_at_level(level: int) -> float:
    if level <= 0:
        if level < 0:
            raise ValueError(f'Level Cannot Be Smaller Than Zero! Level: {level}')
        return 0
    return int(level * COMMON_DIFFERENCE_PER_LEVEL + recursively_calculate_total_exp_at_level(level - 1))


def non_recursively_calculate_total_exp_at_level(level: int) -> float:
    """
    A Quadratic Equation That Calculates The Total EXP Accrued At Level :level:.

    >>> COMMON_DIFFERENCE_PER_LEVEL = 125
    >>> non_recursively_calculate_total_exp_at_level(3)
    750
    """
    if level < 0:
        raise ValueError(f'Level Cannot Be Smaller Than Zero! Level: {level}')
    return COMMON_DIFFERENCE_PER_LEVEL / 2 * level ** 2 + COMMON_DIFFERENCE_PER_LEVEL / 2 * level


def calculate_level_from_total_exp(experience: float) -> int:
    """
    A Quadratic Equation That Calculates The Level That The :class:`Entity`
    Should Be At Given The Accrued Experience.

    >>> COMMON_DIFFERENCE_PER_LEVEL = 125
    >>> calculate_level_from_total_exp(750)
    3
    """
    return floor(
        (
            -(COMMON_DIFFERENCE_PER_LEVEL / 2)
            +
            sqrt(
                (COMMON_DIFFERENCE_PER_LEVEL / 2) ** 2 - (4 * (COMMON_DIFFERENCE_PER_LEVEL / 2) * -experience)
            )
        )
        /
        (
            2 * (COMMON_DIFFERENCE_PER_LEVEL / 2)
        )
    )
