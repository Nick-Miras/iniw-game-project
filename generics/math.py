from math import floor, sqrt


def quadratic_equation_from_quadratic_sequence_using(common_difference: int, y: float) -> int:
    return floor(
        (
                -(common_difference / 2)
                +
                sqrt(
                    (common_difference / 2) ** 2 - (4 * (common_difference / 2) * -y)
                )
        )
        /
        (
                2 * (common_difference / 2)
        )
    )


def get_y_from_quadratic_sequence_using(common_difference: int, x: int):
    return int(common_difference / 2 * x ** 2 + common_difference / 2 * x)
