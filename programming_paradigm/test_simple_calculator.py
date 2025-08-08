import unittest
from simple_calculator import SimpleCalculator





class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)

    def test_minus(self):
        result = self.calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = self.calc.multiply(5, 2)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)

    def test_divide_zero(self):
        result = self.calc.divide(10, 0)
        self.assertEqual(result, None)



if __name__ == "__main__":
    unittest.main()