"""Tests for weight conversion functions"""

import pytest
from converters.weight import kilograms_to_pounds, pounds_to_kilograms


class TestKilogramsToPounds:
    """Test cases for kilograms to pounds conversion"""
    
    def test_zero_weight(self):
        assert kilograms_to_pounds(0) == 0.0
    
    def test_one_kilogram(self):
        result = kilograms_to_pounds(1)
        assert 2.20 <= result <= 2.21
    
    def test_ten_kilograms(self):
        result = kilograms_to_pounds(10)
        assert 22.04 <= result <= 22.05
    
    def test_negative_weight(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            kilograms_to_pounds(-5)


class TestPoundsToKilograms:
    """Test cases for pounds to kilograms conversion"""
    
    def test_zero_weight(self):
        assert pounds_to_kilograms(0) == 0.0
    
    def test_one_pound(self):
        result = pounds_to_kilograms(1)
        assert 0.45 <= result <= 0.46
    
    def test_ten_pounds(self):
        result = pounds_to_kilograms(10)
        assert 4.53 <= result <= 4.54
    
    def test_negative_weight(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            pounds_to_kilograms(-5)