import pytest
from build import build_decks


def test_missing_lands_list():
    """Is an exception raised when there are no reserved land cards provided?"""
    with pytest.raises(
        Exception,
        match="10 land cards are required for the sideboard! Check your Battle Box list!",
    ):
        build_decks(["spell_1", "spell_2"], ["spell_1", "spell_2"], [])


def test_not_enough_lands():
    """Is an exception raised when there are not enough reserved land cards provided?"""
    with pytest.raises(
        Exception,
        match="10 land cards are required for the sideboard! Check your Battle Box list!",
    ):
        build_decks(["spell_1", "spell_2"], ["spell_1", "spell_2"], ["1 Mountain"])
