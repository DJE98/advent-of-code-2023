from typing import Tuple, List


class GamesAnalyser:
    def __init__(self, games: Tuple[Tuple[int, Tuple[Tuple[int, ...], ...]], ...]):
        self.games = games

    def search_possible_games(self, max_round: Tuple[int, ...]) -> Tuple:
        valid_games = []
        for game in self.games:
            game_rounds = game[1]
            game_number = game[0]
            valid = self.check_game_rounds_valid(game_number, game_rounds, max_round)
            if valid:
                valid_games.append(game_number)
        return tuple(valid_games)

    def check_game_rounds_valid(
        self, game_number: int, game_rounds: Tuple[Tuple[int, ...], ...], max_round
    ) -> bool:
        valid = True
        for game_round in game_rounds:
            self.expect_equal_round_size(game_number, game_round, max_round)
            for color_value, max_color_value in zip(game_round, max_round):
                if color_value > max_color_value:
                    valid = False
                    break
        return valid

    def expect_equal_round_size(
        self, game_number: int, game_round: Tuple[int, ...], max_round: Tuple[int, ...]
    ) -> None:
        if len(game_round) != len(max_round):
            raise TypeError(
                f"Game {game_number}: {game_round} not {len(max_round)} length"
            )

    def search_minimal_requirements(self):
        minimal_requirements = []
        for game in self.games:
            game_rounds = game[1]
            minimal_requirement = self.search_minimal_requirements_per_rounds(
                game_rounds
            )
            minimal_requirements.append(minimal_requirement)
        return tuple(minimal_requirements)

    def search_minimal_requirements_per_rounds(
        self, game_rounds: Tuple[Tuple[int, ...], ...]
    ):
        min_values: List[int] = [0 for _ in range(len(game_rounds[0]))]
        for game_round in game_rounds:
            for i, color in enumerate(game_round):
                if color > min_values[i]:
                    min_values[i] = color
        return tuple(min_values)
