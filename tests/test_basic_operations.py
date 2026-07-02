"""Unit tests for basic calculator operations."""

import unittest
from calculator.basic_operations import BasicCalculator


class TestBasicOperations(unittest.TestCase):
    """Test cases for BasicCalculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = BasicCalculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10.5, 2.5), 13.0)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-5, 3), -2)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)


if __name__ == "__main__":
    unittest.main()
