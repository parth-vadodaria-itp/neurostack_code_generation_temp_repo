"""Integration tests for the unified Calculator class."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the unified Calculator interface."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_all_basic_operations(self):
        """Test all basic operations through unified interface."""
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.multiply(10, 5), 50)
        self.assertEqual(self.calc.divide(10, 5), 2)

    def test_all_advanced_operations(self):
        """Test all advanced operations through unified interface."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.square(5), 25)
        self.assertEqual(self.calc.square_root(25), 5)

    def test_error_handling(self):
        """Test error handling through unified interface."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.square_root(-25)

    def test_chained_operations(self):
        """Test multiple operations in sequence."""
        result = self.calc.add(5, 3)
        result = self.calc.multiply(result, 2)
        result = self.calc.square(result)
        self.assertEqual(result, 256)


if __name__ == "__main__":
    unittest.main()
