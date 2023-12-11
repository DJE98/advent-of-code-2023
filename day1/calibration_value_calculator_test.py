""" Implementation of the example as unit test from the first day of advent of code 2023 in Python"""

import unittest
from calibration_value_calculator import CalibrationValueCalculator


class CalibrationValueCalculatorTest(unittest.TestCase):
    """Tests the Functionality of the CalibrationValueCalculator"""

    def test_example(self):
        """Implements the example from the website as unit test"""
        calibration_value_calculator = CalibrationValueCalculator("day1/example1.txt")
        self.assertEqual(
            calibration_value_calculator(),
            142,
            "The solution for the example should be 142",
        )
        
    def test_example2(self):
        """Implements the example from the website as unit test"""
        calibration_value_calculator = CalibrationValueCalculator("day1/example2.txt")
        self.assertEqual(
            calibration_value_calculator(),
            281,
            "The solution for the example should be 281",
        )


if __name__ == "__main__":
    unittest.main()
