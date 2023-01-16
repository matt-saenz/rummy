"""Script for plotting a game of rummy."""


import sys

import matplotlib.pyplot as plt

from rummy import RummyGame


script = sys.argv[0]
args = sys.argv[1:]
usage = f"Usage: {script} game_file"

if not args:
    sys.exit(usage)

game_file = args[0]


game = RummyGame(game_file)

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
