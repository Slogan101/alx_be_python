import unittest
from simple_calculator import SimpleCalculator

class TestAdd(unittest.TestCase):

    def test_add(self):
        result = SimpleCalculator.add(self, 5, 3)
        self.assertEqual(result, 8)

    def test_minus(self):
        result = SimpleCalculator.subtract(self, 5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        result = SimpleCalculator.multiply(self, 5, 2)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = SimpleCalculator.divide(self, 10, 2)
        self.assertEqual(result, 5)

    def test_divide_zero(self):
        result = SimpleCalculator.divide(self, 10, 0)
        self.assertEqual(result, None)



if __name__ == "__main__":
    unittest.main()