# battlebox

A simple program to prepare two-player digital MTG Battle Box decks in .txt format. 
Card decks are intended to be uploaded to tabletop apps that accept .txt deck formats, such as [Cockatrice](https://cockatrice.github.io/).

## What is Battle Box?
Battle Box is a Magic The Gathering (MTG) format of play where two players share a large card deck. Check out more info on the battle box format from [Lucky Paper](https://luckypaper.co/articles/a-guide-to-battle-box/) and [Casual Cardboard](https://www.youtube.com/watch?v=_3K75KYFoAk).

Tabletop apps typically won't have features for players to share a deck like how a battle box deck would be played in-person. To help make battle box playable digitally, this program can take a full battle box .txt card list,shuffle it, and prepare two .txt deck lists ready for each player to upload. Land cards are placed in each player's list so they can be played from the sideboard in-game. 

Battle box games tend to be short; using this program helps speed up deck prep in-between games.

## Installation
1. This project uses [uv](https://docs.astral.sh/uv/) to manage the project, its virtual environment and packages. Install uv from [here](https://docs.astral.sh/uv/getting-started/installation/). Once uv is installed, all that is required is activating the virtual environment in Step #3 below.

2. Clone the repository:
```sh
git clone <repository-url>
cd battlebox
```

3. Create the virtual environment with uv:
```sh
uv sync
```

## Usage
1. The input and output .txt directories are managed as environment variables. Create a .env file in battlebox root directory and create three variables:
```env
LOAD_PATH={path to battlebox deck list .txt}
P1_WRITE_PATH={path to player 1 deck list .txt}
P1_WRITE_PATH={path to player 2 deck list .txt}
```

2. Run the program:
```sh
uv run src/main.py
```

## Sample Deck List
[CasualBattleBox.txt](https://github.com/bmpower/battlebox/blob/master/CasualBattleBox.txt) shows a sample battlebox deck list for input.

