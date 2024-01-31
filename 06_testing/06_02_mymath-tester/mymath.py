# Write a unittest test suite in `test_mymath.py`
# for the `subtract_divide()` function shown below.
# Check for more instructions in `test_mymath.py`

class CustomZeroDivsionError(Exception):
    pass


def subtract_divide(dividend, x, y):
    try:
        z = x - y
        return dividend / z
    except ZeroDivisionError:
        raise CustomZeroDivsionError(f"This won't work because {x} - {y} = 0.")
    

import unittest
from mymath subtract_divide, CustomZeroDivsionError


class TestSubtractDivide(unittest.TestCase):
    def test_subtract_divide_result(self):
        result = subtract_divide(10, 5, 3)
        self.assertEqual(result, 5, 'this is the result 5')

#HELP