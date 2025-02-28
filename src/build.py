def build_decks(p1_spells: list, p2_spells: list, lands: list) -> tuple[list, list]:
    """Build full deck of spell and land cards, and convert to format required for .txt"""

    # Add land values to spell lists - this modifies the spell lists.
    p1_spells.extend(lands)
    p2_spells.extend(lands)

    # Insert a space between spells and lands - this is required in .txt for deck upload.
    # Lands are always the last 10 cards in the list (to be placed in sideboard).
    if lands and len(lands) == 10:
        p1_spells.insert(-10, "")
        p2_spells.insert(-10, "")
    # If there are no lands or less than 10 given, add a message stating requirements.
    else:
        raise Exception(
            "10 land cards are required for the sideboard! Check your Battle Box list!"
        )

    # Convert final list into string for .txt with newline separator.
    p1_deck = "\n".join(p1_spells)
    p2_deck = "\n".join(p2_spells)

    return p1_deck, p2_deck
