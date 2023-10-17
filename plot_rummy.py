"""Script for plotting a game of rummy."""


import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt

from rummy import RummyGame


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("game_file", type=Path)
    args = parser.parse_args()
    return args


def load_game(game_file: Path) -> RummyGame:
    game = RummyGame(game_file)

    if game.empty:
        sys.exit("Error: Cannot make plot for empty game")

    return game


def plot_scorecard(game: RummyGame) -> None:
    scorecard = game.scorecard

    for player, scores in scorecard.items():
        plt.plot(scores, label=player, marker=".")

    plt.xlabel("Hand")
    plt.ylabel("Cumulative score")
    plt.legend()
    plt.grid()

    plt.show()  # type: ignore[no-untyped-call]


def main() -> None:
    args = get_args()
    game = load_game(args.game_file)
    plot_scorecard(game)


if __name__ == "__main__":
    main()
