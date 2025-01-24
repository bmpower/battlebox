import random


def shuffle_and_split_spells(spells: list) -> tuple[list, list]:
    """Shuffle spell cards and split them in half"""
    random.shuffle(spells)

    # Split the shuffled cards in half - p1 gets 1st half, p2 gets 2nd half.
    p1_spells = spells[: (len(spells) // 2)]
    p2_spells = spells[(len(spells) // 2) :]

    return p1_spells, p2_spells
