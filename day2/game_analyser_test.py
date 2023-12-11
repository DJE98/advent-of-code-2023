import unittest

from game_analyser import GamesAnalyser
from game_parser import GameParser


class GameAnalyserTest(unittest.TestCase):
    def test_valid_games(self):
        games = (
            (1, ((12, 13, 14), (12, 13, 14), (12, 13, 14))),
            (2, ((12, 13, 14), (12, 13, 14), (12, 13, 14))),
            (3, ((12, 13, 14), (12, 13, 14), (12, 13, 14))),
        )
        game_analyser = GamesAnalyser(games)
        self.assertEqual(game_analyser.search_possible_games((12, 13, 14)), (1, 2, 3))

    def test_first_value_to_high_in_games(self):
        games = (
            (1, ((13, 13, 14), (12, 13, 14), (12, 13, 14))),
            (2, ((12, 13, 14), (13, 13, 14), (12, 13, 14))),
            (3, ((12, 13, 14), (12, 13, 14), (13, 13, 14))),
        )
        game_analyser = GamesAnalyser(games)
        self.assertEqual(game_analyser.search_possible_games((12, 13, 14)), ())

    def test_second_value_to_high_in_games(self):
        games = (
            (1, ((0, 14, 0), (0, 0, 0), (0, 0, 0))),
            (2, ((0, 0, 0), (0, 14, 0), (0, 0, 0))),
            (3, ((0, 0, 0), (0, 0, 0), (0, 14, 0))),
        )
        game_analyser = GamesAnalyser(games)
        self.assertEqual(game_analyser.search_possible_games((12, 13, 14)), ())

    def test_example(self):
        example_games = (
            (1, ((4, 3, 0), (1, 6, 2), (0, 0, 2))),
            (2, ((0, 1, 2), (1, 4, 3), (0, 1, 1))),
            (3, ((20, 6, 8), (4, 5, 13), (1, 0, 5))),
            (4, ((3, 6, 1), (6, 0, 3), (14, 15, 3))),
            (5, ((6, 1, 3), (1, 2, 2))),
        )
        game_analyser = GamesAnalyser(example_games)
        self.assertEqual(game_analyser.search_possible_games((12, 13, 14)), (1, 2, 5))

    def test_example_two(self):
        game_two = (
            (1, ((4, 0, 3), (1, 2, 6), (0, 2, 0))),
            (2, ((0, 2, 1), (1, 3, 4), (0, 1, 1))),
            (3, ((20, 8, 6), (4, 13, 5), (1, 5, 0))),
            (4, ((3, 1, 6), (6, 3, 0), (14, 3, 15))),
            (5, ((6, 3, 1), (1, 2, 2))),
        )
        game_analyser = GamesAnalyser(game_two)
        minimal_requirements = game_analyser.search_minimal_requirements()
        print(minimal_requirements)
        self.assertEqual(minimal_requirements, ((4,2,6),(1,3,4), (20,13,6), (14,3,15), (6,3,2)))


if __name__ == "__main__":
    unittest.main()
