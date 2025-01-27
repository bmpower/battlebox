from pathlib import Path


def load_cards(load_path: str) -> list[str]:
    """Load the full battlebox cards .txt file from specified path and convert it to a list"""
    path = Path(load_path)

    # Get cards into a list.
    cards = path.read_text().splitlines()

    return cards
