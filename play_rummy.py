"""Script for playing a game of rummy using the rummy module."""


import sys

from rummy import RummyGame
from utils import get_int, get_y_n


# Prelims

script = sys.argv[0]
args = sys.argv[1:]
usage = f"Usage: {script} target_score game_file"

if not args:
    sys.exit(usage)

if len(args) != 2:
    sys.exit("Error: Exactly two args required")

target_score_in, game_file = args


# Set up game

try:
    target_score = int(target_score_in)
except ValueError:
    sys.exit("Error: target_score must be an integer")


try:
    game = RummyGame(game_file)
except FileNotFoundError:
    create = get_y_n(f"{game_file} not found, create new file (y/n)? ")

    if create == "n":
        sys.exit(0)

    game = RummyGame()
else:
    print(f"Loaded a previous game from {game_file}")


if game.empty:
    while True:
        player = input("Enter the name of a player to add to the game: ")

        starting_score = get_int(
            f"Enter the starting score for {player} (or nothing for 0): ",
            allow_empty=True,
        )

        game.add_player(player, starting_score)

        if len(game.players) >= 2:
            add_another = get_y_n("Add another player to the game (y/n)? ")

            if add_another == "n":
                break


# Start game

print(f"\nStarting scoreboard:\n{game}")
print(f"Target score to win the game is {target_score}\n")

winner = game.find_winner(target_score)

if winner:
    print(f"{winner} already has a winning score!")
    sys.exit(0)

while True:
    scores = {}

    for player in game.players:
        score = get_int(f"Enter the score for {player}: ")
        scores[player] = score

    print()  # For spacing
    record = get_y_n("Record the above scores (y/n)? ")

    if record == "n":
        print("Aborted recording the above scores")
        sys.exit(0)

    for player, score in scores.items():
        game.add_score(player, score)

    game.save(game_file)

    print(f"\nUpdated scoreboard:\n{game}\n")
    print(f"(progress saved to {game_file})\n")

    winner = game.find_winner(target_score)

    if winner:
        print(f"{winner} won the game!")
        break

    cont = get_y_n("Continue playing (y/n)? ")

    if cont == "n":
        break

    print()  # For spacing, before next round
