"""Tests for length conversion functions"""

import pytest
from converters.length import centimeters_to_inches, inches_to_centimeters


class TestCentimetersToInches:
    """Test cases for centimeters to inches conversion"""
    
    def test_zero_length(self):
        assert centimeters_to_inches(0) == 0.0
    
    def test_one_centimeter(self):
        result = centimeters_to_inches(1)
        assert 0.39 <= result <= 0.40
    
    def test_ten_centimeters(self):
        result = centimeters_to_inches(10)
        assert 3.93 <= result <= 3.94
    
    def test_negative_length(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            centimeters_to_inches(-5)


class TestInchesToCentimeters:
    """Test cases for inches to centimeters conversion"""
    
    def test_zero_length(self):
        assert inches_to_centimeters(0) == 0.0
    
    def test_one_inch(self):
        result = inches_to_centimeters(1)
        assert result == 2.54
    
    def test_ten_inches(self):
        result = inches_to_centimeters(10)
        assert result == 25.4
    
    def test_negative