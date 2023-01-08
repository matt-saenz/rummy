# rummy :hearts: :clubs: :diamonds: :spades:

## Overview

[Script](play_rummy.py) for tracking games of rummy (500 style) powered by a [module](rummy.py) defining a `RummyGame` class.

## Script Usage

```
python play_rummy.py target_score game_file
```

`target_score` is the score needed to win the game. `game_file` is the file to save game progress to. If `game_file` specifies a file that already exists, a previous game is loaded from the file and resumed. Game files are in JSON and record the cumulative scores of each game player. For example:

```json
{
    "Player 1": [
        0,
        85,
        65
    ],
    "Player 2": [
        0,
        100,
        190
    ]
}
```
