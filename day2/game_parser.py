from typing import Tuple, List


class GameParser:
    colors = ("red", "green", "blue")
    min_round_size = 2
    round_separator_symbol = ";"
    round_start_symbol = ":"
    color_separator_symbol = ","

    def parse_file(self, filename: str) -> Tuple[Tuple[int, Tuple[Tuple[int, ...], ...]], ...]:
        with open(filename, "r", encoding="utf-8") as file:
            games = self.parse_games(file.readlines())
        return games

    def parse_games(self, game_strings: List[str]) -> Tuple[Tuple[int, Tuple[Tuple[int, ...], ...]], ...]:
        games = []
        for game_string in game_strings:
            games.append(self.parse_game(game_string))
        return tuple(games)

    def parse_game(self, game_string: str) -> Tuple[int, Tuple[Tuple[int, ...], ...]]:
        game_header, game_body = game_string.split(self.round_start_symbol)
        game_number = self.parse_game_header(game_header)
        round_strings = game_body.split(self.round_separator_symbol)
        self.check_round_size(round_strings)
        game_rounds = self.parse_rounds(round_strings)
        return (game_number, game_rounds)
    
    def parse_game_header(self, game_header:str) -> int:
        position = game_header.find("Game")
        if position == -1:
            raise ValueError("Game Number not found")
        game_number = int(game_header[position + len("Game"): ])
        return game_number

    def check_round_size(self, round_strings) -> None:
        if len(round_strings) < self.min_round_size:
            raise ValueError(f"At least {self.min_round_size} rounds per game expected")

    def parse_rounds(self, round_strings: List[str]) -> Tuple[Tuple[int, ...], ...]:
        game_rounds = []
        for round_string in round_strings:
            game_rounds.append(self.parse_round(round_string))
        return tuple(game_rounds)

    def parse_round(self, round_string: str) -> Tuple[int, ...]:
        color_values = {}
        color_strings = round_string.split(self.color_separator_symbol)
        for color in self.colors:
            color_values[color] = 0
            for color_string in color_strings:
                try:
                    color_value = self.parse_color(color_string, color)
                    color_values[color] = color_value
                except ValueError:
                    pass
        return tuple(color_values[color] for color in self.colors)

    def parse_color(self, color_string: str, color: str) -> int:
        position = color_string.find(color)
        if position == -1:
            raise ValueError
        color_value = int(color_string[0:position])
        return color_value

    def __call__(self, filename: str) -> Tuple[Tuple[int, Tuple[Tuple[int, ...], ...]], ...]:
        return self.parse_file(filename)
    
if __name__ == "__main__":
    game_parser = GameParser()
    input_one_games = game_parser("day2/input1.txt")
    for input_one_game in input_one_games:
        print(input_one_game)

