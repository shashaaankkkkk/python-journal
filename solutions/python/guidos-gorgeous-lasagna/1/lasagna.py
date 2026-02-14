"""
Functions used in preparing Guido's gorgeous lasagna.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """
    Calculate remaining bake time.

    :param elapsed_bake_time: int - minutes already baked
    :return: int - remaining bake time
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(layers: int) -> int:
    """
    Calculate preparation time.

    :param layers: int - number of lasagna layers
    :return: int - total preparation time
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int) -> int:
    """
    Calculate total elapsed cooking time.

    :param layers: int - number of layers
    :param elapsed_bake_time: int - baking time already elapsed
    :return: int - total elapsed time
    """
    return preparation_time_in_minutes(layers) + elapsed_bake_time
