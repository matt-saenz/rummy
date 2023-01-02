"""Script for playing a game of rummy using the rummy module."""


from datetime import datetime
import sys

from rummy import RummyGame
from utils import get_int, get_y_n


# Prelims

script = sys.argv[0]
args = sys.argv[1:]
usage = f"Usage: {script} target_score [game_file]"

if not args:
    sys.exit(usage)

if len(args) > 2:
    sys.exit("Error: Too many args given")

target_score_in = args[0]
game_file = args[1] if len(args) == 2 else None


# Set up game

try:
    target_score = int(target_score_in)
except ValueError:
    sys.exit("Error: target_score must be an integer")


ts = datetime.now().strftime("%Y_%m_%d_%H_%M")
file_name = f"rummy_{ts}.json"


if game_file:
    game = RummyGame(game_file)
    print(f"Loaded a previous game from {game_file}")
else:
    game = RummyGame()
    print("Starting a new game of rummy")

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
    print(f"{winner} already has a winning score!\n")
else:
    while True:
        for player in game.players:
            score = get_int(f"Enter the score for {player}: ")
            game.add_score(player, score)

        print(f"\nUpdated scoreboard:\n{game}\n")

        winner = game.find_winner(target_score)

        if winner:
            print(f"{winner} won the game!\n")
            break

        cont = get_y_n("Continue playing (y/n)? ")

        print()  # For spacing

        if cont == "n":
            break


# Save game

save = get_y_n("Save the game to a file (y/n)? ")

if save == "n":
    sys.exit(0)

if game_file:
    overwrite = get_y_n(f"Overwrite {game_file} (y/n)? ")

    if overwrite == "y":
        game.save(game_file)
        print(f"Saved game to {game_file}")
        sys.exit(0)

use_gen = get_y_n(f"Use generated file name {file_name} (y/n)? ")

if use_gen == "n":
    file_name = input("Enter your preferred file name: ")

game.save(file_name)

print(f"Saved game to {file_name}")
