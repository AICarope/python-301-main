# Write two unittest test cases for the `subtract_divide()` function
# in `mymath.py`
#
# 1. Check for correct results by providing example input.
# 2. Check that a `CustomZeroDivisionError` gets raised correctly.

#to create initest test cases I need to import unitest module>create a class as inheritate > create methods

import unittest
from mymath import subtract_divide(), CustomZeroDivisionError

class TestSubtractDivide(unittest.TestCase):
    #TestCase 1: check results for the function 
    def test_subtract_divide_result(self): 
        self.assertEqual(subtract_divide(10, 5, 3, 'teh function returns 5'))

     #TestCase 2: check results for CustomZeroDivisionError
    def test_zero_division_error(self): 
        with self.assertRaises(CustomZeroDivisionError):
            subtract_divide(10, 2, 6)