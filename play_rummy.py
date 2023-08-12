"""Script for playing a game of rummy using the rummy module."""


import argparse
import sys
from pathlib import Path

from rummy import RummyGame


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument("target_score", type=int)
    parser.add_argument("game_file", type=Path)

    args = parser.parse_args()

    return args


def set_up_game(game_file: Path) -> RummyGame:
    if not game_file.exists():
        create = confirm(f"{game_file} does not exist, create new file")

        if not create:
            sys.exit(0)

        game = RummyGame()
    else:
        game = RummyGame(game_file)
        print(f"Loaded a previous game from {game_file}")

    if game.empty:
        while True:
            player = input("Enter the name of a player to add to the game: ")

            starting_score = get_int(
                f"Enter the starting score for {player} (or nothing for 0)",
                allow_empty=True,
            )

            game.add_player(player, starting_score)

            if len(game.players) >= 2:
                add_another = confirm("Add another player to the game")

                if not add_another:
                    break

    return game


def play_game(
    game: RummyGame,
    game_file: Path,
    target_score: int,
) -> None:
    print(f"\nStarting scoreboard:\n{game}")
    print(f"Target score to win the game is {target_score}\n")

    winner = game.find_winner(target_score)

    if winner:
        print(f"{winner} already has a winning score!")
        sys.exit(0)

    while True:
        scores = {}

        for player in game.players:
            score = get_int(f"Enter the score for {player}")
            scores[player] = score

        print()  # For spacing
        record = confirm("Record the above scores")

        if not record:
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

        cont = confirm("Continue playing")

        if not cont:
            break

        print()  # For spacing, before next round


def get_int(message: str, allow_empty: bool = False) -> int:
    resp = input(message + ": ")

    if allow_empty:
        if resp == "":
            return 0

    while True:
        try:
            integer = int(resp)
            break
        except ValueError:
            resp = input("Oops! Input must be an integer. Please try again: ")

    return integer


def confirm(message: str) -> bool:
    resp = input(message + " (y/n)? ")

    while True:
        if resp in {"y", "n"}:
            break

        resp = input("Oops! Valid inputs are 'y' or 'n'. Please try again: ")

    return resp == "y"


def main() -> None:
    args = get_args()
    game = set_up_game(args.game_file)
    play_game(game, args.game_file, args.target_score)


if __name__ == "__main__":
    main()
