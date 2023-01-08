"""Module defining RummyGame class."""


import copy
import json


class RummyGame:
    """A RummyGame object represents a game of rummy."""

    def __init__(self, game_file: str | None = None):
        """Create a new RummyGame object."""

        if game_file is None:
            self._scorecard = {}
        else:
            with open(game_file) as f:
                self._scorecard = json.load(f)

    @property
    def empty(self) -> bool:
        """Indicates whether the game is empty (no players added yet)."""
        return not self._scorecard

    def add_player(self, name: str, starting_score: int) -> None:
        """Add a player to the game with a starting score."""

        if name in self._scorecard:
            raise RummyGameError(f"A player named '{name}' is already in the game")

        if not isinstance(starting_score, int):
            raise RummyGameError("starting_score must be an int")

        self._scorecard[name] = [starting_score]

    @property
    def players(self) -> list:
        """List of players in the game."""
        return list(self._scorecard)

    def add_score(self, player: str, score: int) -> None:
        """Add a player's score to the scorecard."""

        if player not in self._scorecard:
            raise RummyGameError(f"No player named '{player}' in the game")

        if not isinstance(score, int):
            raise RummyGameError("score must be an int")

        prev_score = self._scorecard[player][-1]
        self._scorecard[player].append(prev_score + score)

    @property
    def scorecard(self) -> dict:
        """
        Game scorecard (cumulative scores).

        Deep copy since scorecard should not be manipulated directly.
        """
        return copy.deepcopy(self._scorecard)

    @property
    def scoreboard(self) -> dict:
        """Game scoreboard (latest score only)."""
        scoreboard = {}

        for player, scores in self._scorecard.items():
            scoreboard[player] = scores[-1]

        return scoreboard

    def __str__(self):
        list_of_scores = []

        for player, score in self.scoreboard.items():
            list_of_scores.append(f"{player}: {score}")

        return "\n".join(list_of_scores)

    def find_winner(self, target_score: int) -> str | None:
        """
        Find a game winner given the target score.

        Returns None if there is no winner yet, otherwise the name
        of the winner.
        """

        if not isinstance(target_score, int):
            raise RummyGameError("target_score must be an int")

        scoreboard = self.scoreboard

        max_score = max(scoreboard.values())

        if max_score < target_score:
            return None

        max_scorers = []

        for player, score in scoreboard.items():
            if score == max_score:
                max_scorers.append(player)

        if len(max_scorers) == 1:
            return max_scorers[0]
        else:
            # There is a tie!
            return None

    def save(self, game_file: str) -> None:
        """Save the game scores to a file in JSON."""

        with open(game_file, "w") as f:
            json.dump(self._scorecard, f, indent=4)
            f.write("\n")

    def __eq__(self, other):
        if not isinstance(other, RummyGame):
            return NotImplemented

        return self._scorecard == other._scorecard


class RummyGameError(Exception):
    """Raise if something goes wrong with a RummyGame object."""
