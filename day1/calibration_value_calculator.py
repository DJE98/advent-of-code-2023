""" Implementation of the first day of advent of code 2023 in Python"""


class CalibrationValueCalculator:
    """Class to calculate the calibration value for a given filename"""

    written_digits = (
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    )

    def __calculate_line_value(self, line: str) -> int:
        """Calculates the calibration value for a specific line"""
        digits = []
        for position, character in enumerate(line):
            if character.isdigit():
                digits.append(int(character))
                continue
            for number in range(1, 10):
                if line[position:].startswith(self.written_digits[number - 1]):
                    digits.append(number)

        return digits[0] * 10 + digits[-1]

    def __calculate_calibration_value(self, filename: str) -> int:
        """Calculates the calibration value for the whole document"""
        calibration_value = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file.readlines():
                calibration_value += self.__calculate_line_value(line)
        return calibration_value

    def __call__(self, filename: str):
        return self.__calculate_calibration_value(filename)
