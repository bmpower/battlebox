from separate import separate_lands_spells

def test_list_with_no_land_cards():
    """Does an input list with no land cards return an empty list?"""
    test_tuple = separate_lands_spells(['creature', 'instant', 'sorcery'])
    assert test_tuple[0] == []

def test_list_with_land_card():
    """Does an input list with at least one reserved land card return a list for lands?"""
    test_tuple = separate_lands_spells(['1 Mountain', 'creature', 'instant'])
    assert test_tuple[0] == ['1 Mountain']



