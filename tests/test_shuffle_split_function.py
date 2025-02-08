from shuffle import shuffle_and_split_spells


def test_list_with_one_element():
    """Does an input list with odd card count always return a larger list for player 2?"""
    """Make sure the full deck list has an even count of non-land cards for fair play!"""
    test_tuple_input_list_of_5 = shuffle_and_split_spells(
        [
            "card",
            "card",
            "card",
            "card",
            "card",
        ]
    )
    test_tuple_input_list_of_15 = shuffle_and_split_spells(
        [
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
            "card",
        ]
    )

    # Function shuff_and_split_spells() splits the randomized input list in half using len(list) // 2
    # Operator // uses floor division, so an input list with an odd element count should result in fewer elements on the first half of the sliced list.
    assert test_tuple_input_list_of_5[0] < test_tuple_input_list_of_5[1]
    assert test_tuple_input_list_of_15[0] < test_tuple_input_list_of_15[1]
