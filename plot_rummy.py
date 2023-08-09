"""Script for plotting a game of rummy."""


import argparse
import sys
from pathlib import Path

import matplotlib.pyplot as plt

from rummy import RummyGame


parser = argparse.ArgumentParser()
parser.add_argument("game_file", type=Path)
args = parser.parse_args()


game = RummyGame(args.game_file)

if game.empty:
    sys.exit("Error: Cannot make plot for empty game")

scorecard = game.scorecard


for player, scores in scorecard.items():
    plt.plot(scores, label=player, marker=".")

plt.xlabel("Hand")
plt.ylabel("Cumulative score")
plt.legend()
plt.grid()

plt.show()
