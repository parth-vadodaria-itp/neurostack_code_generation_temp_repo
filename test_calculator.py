"""
Unit tests for the Calculator class.
"""
import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()
    
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
    
    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
    
    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))
    
    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)
    
    def test_modulo_negative_numbers(self):
        """Test modulo operation with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)
    
    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertIn("Cannot perform modulo with zero divisor", str(context.exception))
    
    def test_square_positive_numbers(self):
        """Test square of positive numbers."""
        self.assertEqual(self.calc.square(5), 25)
        self.assertEqual(self.calc.square(2.5), 6.25)
    
    def test_square_negative_numbers(self):
        """Test square of negative numbers."""
        self.assertEqual(self.calc.square(-5), 25)
        self.assertEqual(self.calc.square(-3), 9)
    
    def test_square_zero(self):
        """Test square of zero."""
        self.assertEqual(self.calc.square(0), 0)
    
    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers."""
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
