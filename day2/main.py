from game_parser import GameParser
from game_analyser import GamesAnalyser

from typing import Tuple


def calculate_second_solution(minimal_requirements: Tuple[Tuple[int, ...], ...]) -> int:
    multiplied_minimal_requirements = []
    for minimal_requirement in minimal_requirements:
        multiplied_minimal_requirement = 1
        for color in minimal_requirement:
            multiplied_minimal_requirement = color * multiplied_minimal_requirement
        multiplied_minimal_requirements.append(multiplied_minimal_requirement)
    return sum(multiplied_minimal_requirements)


def print_puzzle_solution():
    game_parser = GameParser()
    input_one_games = game_parser("day2/input1.txt")
    input_two_games = game_parser("day2/input2.txt")
    game_one_analyser = GamesAnalyser(input_one_games)
    possible_games = game_one_analyser.search_possible_games((12, 13, 14))
    solution_one = sum(possible_games)
    game_two_analyser = GamesAnalyser(input_two_games)
    minimal_requirements = game_two_analyser.search_minimal_requirements()
    solution_two = calculate_second_solution(minimal_requirements)

    print("Puzzle 1:")
    print(f"Possible games: {possible_games}")
    print(f"Solution 1: {solution_one}")

    print("Puzzle 2:")
    print(f"Minimal requirements: {minimal_requirements}")
    print(f"Solution 2: {solution_two}")


if __name__ == "__main__":
    print_puzzle_solution()
