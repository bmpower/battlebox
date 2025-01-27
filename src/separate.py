def separate_lands_spells(cards: list) -> tuple[list, list]:
    """Separate land cards and spell cards to prepare for shuffle and split"""

    # These land cards are reserved for each player, every game. Never shuffled.
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

    # Separate lands - these should not be included in shuffle.
    lands = [card for card in cards if card in land_cards]

    # Separate spells - these are included in shuffle.
    # The 'and card' condition is to exclude the space between spells and lands as a card
    spells = [card for card in cards if card not in land_cards and card]

    return lands, spells
