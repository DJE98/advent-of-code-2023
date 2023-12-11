from calibration_value_calculator import CalibrationValueCalculator

def print_puzzle_results() -> None:
    """Print results for both puzzles"""
    calibration_value_calculator = CalibrationValueCalculator()
    calibration_value_1 = calibration_value_calculator("day1/input1.txt")
    calibration_value_2 = calibration_value_calculator("day1/input2.txt")
    print(f"Day 1")
    print(f"Puzzle one: {calibration_value_1}")
    print(f"Puzzle two: {calibration_value_2}")


if __name__ == "__main__":
    print_puzzle_results()