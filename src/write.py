from pathlib import Path


def save_decks(
    deck_1: str, deck_2: str, write_path_1: str, write_path_2: str
) -> None:
    """Save both final decks as a .txt file in specified path"""
    p1_path = Path(write_path_1)
    p2_path = Path(write_path_2)

    p1_path.write_text(deck_1)
    p2_path.write_text(deck_2)
