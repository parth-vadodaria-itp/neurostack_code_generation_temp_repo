"""Tests for distance conversion functions"""

import pytest
from converters.distance import kilometers_to_miles, miles_to_kilometers


class TestKilometersToMiles:
    """Test cases for kilometers to miles conversion"""
    
    def test_zero_distance(self):
        assert kilometers_to_miles(0) == 0.0
    
    def test_one_kilometer(self):
        result = kilometers_to_miles(1)
        assert 0.62 <= result <= 0.63
    
    def test_ten_kilometers(self):
        result = kilometers_to_miles(10)
        assert 6.21 <= result <= 6.22
    
    def test_negative_distance(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            kilometers_to_miles(-5)


class TestMilesToKilometers:
    """Test cases for miles to kilometers conversion"""
    
    def test_zero_distance(self):
        assert miles_to_kilometers(0) == 0.0
    
    def test_one_mile(self):
        result = miles_to_kilometers(1)
        assert 1.60 <= result <= 1.61
    
    def test_ten_miles(self):
        result = miles_to_kilometers(10)
        assert 16.09 <= result <= 16.10
    
    def test_negative_distance(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            miles_to_kilometers(-5)