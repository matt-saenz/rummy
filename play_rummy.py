"""Script for playing a game of rummy using the rummy module."""


import argparse
import sys
from pathlib import Path

import utils
from rummy import RummyGame


# Prelims

parser = argparse.ArgumentParser()
parser.add_argument("target_score", type=int)
parser.add_argument("game_file", type=Path)
args = parser.parse_args()


# Set up game

if not args.game_file.exists():
    create = utils.confirm(f"{args.game_file} does not exist, create new file")

    if not create:
        sys.exit(0)

    game = RummyGame()
else:
    game = RummyGame(args.game_file)
    print(f"Loaded a previous game from {args.game_file}")


if game.empty:
    while True:
        player = input("Enter the name of a player to add to the game: ")

        starting_score = utils.get_int(
            f"Enter the starting score for {player} (or nothing for 0)",
            allow_empty=True,
        )

        game.add_player(player, starting_score)

        if len(game.players) >= 2:
            add_another = utils.confirm("Add another player to the game")

            if not add_another:
                break


# Start game

print(f"\nStarting scoreboard:\n{game}")
print(f"Target score to win the game is {args.target_score}\n")

winner = game.find_winner(args.target_score)

if winner:
    print(f"{winner} already has a winning score!")
    sys.exit(0)

while True:
    scores = {}

    for player in game.players:
        score = utils.get_int(f"Enter the score for {player}")
        scores[player] = score

    print()  # For spacing
    record = utils.confirm("Record the above scores")

    if not record:
        print("Aborted recording the above scores")
        sys.exit(0)

    for player, score in scores.items():
        game.add_score(player, score)

    game.save(args.game_file)

    print(f"\nUpdated scoreboard:\n{game}\n")
    print(f"(progress saved to {args.game_file})\n")

    winner = game.find_winner(args.target_score)

    if winner:
        print(f"{winner} won the game!")
        break

    cont = utils.confirm("Continue playing")

    if not cont:
        break

    print()  # For spacing, before next round
