#1. Created a specific test unit "test_unit_testing"
#2. Import unittest
import unittest
#3. Import the function from unit_testing
from unit_testing import areea_of_circle
from math import pi

#4. Create a class for the test
class Test_Area_of_Circle_input(unittest.TestCase):
    def test_area(self):
        # Test radius >= 0
        self.assertAlmostEqual(areea_of_circle(1), pi)
        self.assertAlmostEqual(areea_of_circle(0), 0)
        self.assertAlmostEqual(areea_of_circle(3.5), pi * 3.5**2)
    def test_values(self):
        #Test that bad values are caught
        self.assertRaises(ValueError, areea_of_circle, -1)


#Go to the directory and run it:
#C:\Users\m1i9n\devnetccna>python -m unittest test_unit_testing.py
#530.929158456675
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.001s

#OK
