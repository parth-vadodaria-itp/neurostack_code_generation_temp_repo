"""Unit tests for advanced calculator operations."""

import unittest
import math
from calculator.advanced_operations import AdvancedCalculator


class TestAdvancedOperations(unittest.TestCase):
    """Test cases for AdvancedCalculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = AdvancedCalculator()

    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)
        self.assertEqual(self.calc.modulo(20, 5), 0)

    def test_modulo_negative_numbers(self):
        """Test modulo operation with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertIn("Cannot calculate modulo with zero divisor", str(context.exception))

    def test_square_positive_numbers(self):
        """Test square operation with positive numbers."""
        self.assertEqual(self.calc.square(5), 25)
        self.assertEqual(self.calc.square(3.5), 12.25)
        self.assertEqual(self.calc.square(0), 0)

    def test_square_negative_numbers(self):
        """Test square operation with negative numbers."""
        self.assertEqual(self.calc.square(-5), 25)
        self.assertEqual(self.calc.square(-3), 9)

    def test_square_root_positive_numbers(self):
        """Test square root operation with positive numbers."""
        self.assertEqual(self.calc.square_root(25), 5)
        self.assertEqual(self.calc.square_root(16), 4)
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2))

    def test_square_root_zero(self):
        """Test square root of zero."""
        self.assertEqual(self.calc.square_root(0), 0)

    def test_square_root_negative_number(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.square_root(-25)
        self.assertIn("Cannot calculate square root of negative number", str(context.exception))


if __name__ == "__main__":
    unittest.main()
