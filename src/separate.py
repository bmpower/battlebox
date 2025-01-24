def separate_lands_spells(cards: list) -> tuple[list, list]:
    """Separate lands and spells to prepare for shuffle and split"""

    land_cards = [
        "1 Island",
        "1 Plains",
        "1 Forest",
        "1 Mountain",
        "1 Swamp",
        "1 Blossoming Sands",
        "1 Tranquil Cove",
        "1 Bloodfell Caves",
        "1 Dismal Backwater",
        "1 Rugged Highlands",
    ]

    # Separate lands - we don't want these included in shuffle and split
    lands = [card for card in cards if card in land_cards]

    # Separate spells - we want these included in shuffle and split
    spells = [card for card in cards if card not in land_cards and card]

    return lands, spells
