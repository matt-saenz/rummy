"""Testing for rummy module."""

import unittest

from rummy import RummyGame, RummyGameError


class TestRummy(unittest.TestCase):
    def setUp(self):
        self.game = RummyGame()

        self.game.add_player("Player 1", 0)
        self.game.add_player("Player 2", 0)

        self.game.add_score("Player 1", 65)
        self.game.add_score("Player 2", 70)

        for player in self.game.players:
            self.game.add_score(player, 10)

    def test_empty(self):
        self.assertFalse(self.game.empty)
        empty_game = RummyGame()
        self.assertTrue(empty_game.empty)

    def test_scorecard(self):
        self.assertEqual(
            self.game.scorecard,
            {
                "Player 1": [0, 65, 75],
                "Player 2": [0, 70, 80],
            },
        )

    def test_scoreboard(self):
        self.assertEqual(
            self.game.scoreboard,
            {"Player 1": 75, "Player 2": 80},
        )

    def test_add_player(self):
        with self.assertRaises(RummyGameError):
            self.game.add_player("", 0)

        with self.assertRaises(RummyGameError):
            self.game.add_player("Player 1", 0)

        with self.assertRaises(RummyGameError):
            self.game.add_player("Player 3", "0")

    def test_add_score(self):
        with self.assertRaises(RummyGameError):
            self.game.add_score("Player 3", 100)

        with self.assertRaises(RummyGameError):
            self.game.add_score("Player 1", "100")

    def test_find_winner(self):
        # No player has won yet
        self.assertIsNone(self.game.find_winner(100))

        # Player 2 is only player with score >= target_score
        self.assertEqual(
            self.game.find_winner(80),
            "Player 2",
        )

        # Both player 1 and player 2 have score >= target_score
        self.assertEqual(
            self.game.find_winner(70),
            "Player 2",
        )

        # Player 1 and player 2 are tied with score >= target_score
        self.game.add_score("Player 1", 5)
        self.assertIsNone(self.game.find_winner(70))

    def test_read_write(self):
        self.game.save("test_game.json")
        test_game = RummyGame("test_game.json")
        self.assertEqual(self.game, test_game)

    def test_str(self):
        self.assertEqual(
            str(self.game),
            "Player 1: 75\nPlayer 2: 80",
        )


if __name__ == "__main__":
    unittest.main()
