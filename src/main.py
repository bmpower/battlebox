import os
from dotenv import load_dotenv

from read import load_cards
from separate import separate_lands_spells
from shuffle import shuffle_and_split_spells
from build import build_decks
from write import save_decks


if __name__ == "__main__":
    # Load environment variables.
    load_dotenv()

    # Assign environment variables.
    load_path = os.getenv("LOAD_PATH")
    p1_write_path = os.getenv("P1_WRITE_PATH")
    p2_write_path = os.getenv("P2_WRITE_PATH")

    # Load cards from full card list and build two decks from it.
    cards = load_cards(load_path)
    lands, spells = separate_lands_spells(cards)
    p1_spells, p2_spells = shuffle_and_split_spells(spells)
    p1_deck, p2_deck = build_decks(p1_spells, p2_spells, lands)

    # Save decks as .txt files ready for upload to Cockatrice.
    save_decks(
        deck_1=p1_deck,
        deck_2=p2_deck,
        write_path_1=p1_write_path,
        write_path_2=p2_write_path,
    )
