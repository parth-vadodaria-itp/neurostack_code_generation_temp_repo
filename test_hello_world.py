#!/usr/bin/env python3
"""Unit tests for hello_world program."""

import unittest
from io import StringIO
import sys

import hello_world


class TestHelloWorld(unittest.TestCase):
    """Test cases for hello_world module."""

    def test_main_prints_hello_world(self):
        """Test that main() prints 'hello_world' to stdout."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        hello_world.main()
        
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "hello_world")

    def test_main_returns_none(self):
        """Test that main() returns None."""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        result = hello_world.main()
        
        sys.stdout = sys.__stdout__
        
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
