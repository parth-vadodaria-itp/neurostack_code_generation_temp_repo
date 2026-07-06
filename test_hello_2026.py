#!/usr/bin/env python3
"""Unit tests for hello_2026.py"""

import unittest
from io import StringIO
import sys
from hello_2026 import main

class TestHello2026(unittest.TestCase):
    """Test cases for the Hello 2026 program."""

    def test_main_output(self):
        """Test that main() prints 'Hello 2026' to stdout."""
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello 2026")

    def test_output_format(self):
        """Test that output ends with newline."""
        captured_output = StringIO()
        sys.stdout = captured_output
        main()
        sys.stdout = sys.__stdout__
        self.assertTrue(captured_output.getvalue().endswith("\n"))

if __name__ == "__main__":
    unittest.main()
