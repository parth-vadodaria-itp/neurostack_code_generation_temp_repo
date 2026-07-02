"""Tests for temperature conversion functions"""

import pytest
from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestCelsiusToFahrenheit:
    """Test cases for Celsius to Fahrenheit conversion"""
    
    def test_freezing_point(self):
        assert celsius_to_fahrenheit(0) == 32.0
    
    def test_boiling_point(self):
        assert celsius_to_fahrenheit(100) == 212.0
    
    def test_negative_temperature(self):
        assert celsius_to_fahrenheit(-40) == -40.0
    
    def test_room_temperature(self):
        assert celsius_to_fahrenheit(25) == 77.0
    
    def test_below_absolute_zero(self):
        with pytest.raises(ValueError, match="absolute zero"):
            celsius_to_fahrenheit(-300)


class TestFahrenheitToCelsius:
    """Test cases for Fahrenheit to Celsius conversion"""
    
    def test_freezing_point(self):
        assert fahrenheit_to_celsius(32) == 0.0
    
    def test_boiling_point(self):
        assert fahrenheit_to_celsius(212) == 100.0
    
    def test_negative_temperature(self):
        assert fahrenheit_to_celsius(-40) == -40.0
    
    def test_room_temperature(self):
        assert fahrenheit_to_celsius(77) == 25.0
    
    def test_below_absolute_zero(self):
        with pytest.raises(ValueError, match="absolute zero"):
            fahrenheit_to_celsius(-500)