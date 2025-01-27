from pathlib import Path


def load_cards(load_path: str) -> list[str]:
    """Load full battlebox card list .txt"""
    path = Path(load_path)
    # Get cards in a list
    cards = path.read_text().splitlines()

    return cards
