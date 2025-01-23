
def build_deck(p1_spells, p2_spells, lands):
    """Build full deck and convert to format required for .txt"""
    
    # Add land values to spell lists - this modifies the spell lists
    p1_spells.extend(lands)
    p2_spells.extend(lands)

    
    # Insert a space between spells and lands - this is required in .txt for deck upload
    # Lands are always the last 10 cards in the list
    p1_spells.insert(-10, '')
    p2_spells.insert(-10, '')

    # Convert final list into string with newline separator for .txt
    p1_deck = '\n'.join(p1_spells)
    p2_deck = '\n'.join(p2_spells)

    return p1_deck, p2_deck