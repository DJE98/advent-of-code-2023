import unittest
from game_parser import GameParser


class GameParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = GameParser()

    def test_parse_color_valid(self):
        color_string = "3 red"
        self.assertEqual(self.parser.parse_color(color_string, "red"), 3)

    def test_parse_color_with_invalid_color(self):
        color_string = "3 yellow"
        with self.assertRaises(ValueError):
            self.parser.parse_color(color_string, "red")

    def test_parse_color_set_default_value(self):
        color_string = " red"
        with self.assertRaises(ValueError):
            self.parser.parse_color(color_string, "red")

    def test_parse_round_valid(self):
        round_string = "3 red, 2 blue, 1 green"
        expected = (3, 2, 1)
        self.assertEqual(self.parser.parse_round(round_string), expected)

    def test_parse_round_with_default(self):
        round_string = "3 red, 1 green"
        expected = (3, 0, 1)
        self.assertEqual(self.parser.parse_round(round_string), expected)

    def test_parse_round_valid_with_other_order(self):
        round_string = "1 green, 2 blue, 3 red"
        expected = (3, 2, 1)
        self.assertEqual(self.parser.parse_round(round_string), expected)

    def test_parse_game_valid(self):
        game_string = "Game 1 : 3 red, 2 blue, 1 green; 0 red, 4 blue, 2 green; 1 red, 0 blue, 3 green"
        expected = (1, ((3, 2, 1), (0, 4, 2), (1, 0, 3)))
        self.assertEqual(self.parser.parse_game(game_string), expected)

    def test_parse_example_one_file_valid(self):
        example_games = (
            (1, ((4, 3, 0), (1, 6, 2), (0, 0, 2))),
            (2, ((0, 1, 2), (1, 4, 3), (0, 1, 1))),
            (3, ((20, 6, 8), (4, 5, 13), (1, 0, 5))),
            (4, ((3, 6, 1), (6, 0, 3), (14, 15, 3))),
            (5, ((6, 1, 3), (1, 2, 2))),
        )
        result = self.parser.parse_file("day2/example1.txt")
        self.assertEqual(result, example_games)


if __name__ == "__main__":
    unittest.main()
