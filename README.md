# rummy :hearts: :clubs: :diamonds: :spades:

## Overview

[Script](play_rummy.py) for tracking games of rummy (500 style) powered by a [module](rummy.py) defining a `RummyGame` class.

## Script Usage

```
python play_rummy.py target_score [game_file]
```

`target_score` is the score needed to win the game. If a game file is given, a previous game is loaded from the file. Otherwise, a new game is started. Game files are in JSON and can be created through usage of the script.
