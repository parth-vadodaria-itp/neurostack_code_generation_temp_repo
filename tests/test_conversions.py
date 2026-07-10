"""
Unit tests for conversion functions.
"""

import pytest
from conversions import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
    kilograms_to_pounds,
    pounds_to_kilograms,
    centimeters_to_inches,
    inches_to_centimeters
)


class TestTemperatureConversions:
    """Test temperature conversion functions."""
    
    def test_celsius_to_fahrenheit_freezing(self):
        """Test water freezing point conversion."""
        assert celsius_to_fahrenheit(0) == 32.0
    
    def test_celsius_to_fahrenheit_boiling(self):
        """Test water boiling point conversion."""
        assert celsius_to_fahrenheit(100) == 212.0
    
    def test_celsius_to_fahrenheit_negative(self):
        """Test negative temperature conversion."""
        result = celsius_to_fahrenheit(-40)
        assert abs(result - (-40.0)) < 0.01
    
    def test_fahrenheit_to_celsius_freezing(self):
        """Test water freezing point conversion."""
        assert fahrenheit_to_celsius(32) == 0.0
    
    def test_fahrenheit_to_celsius_boiling(self):
        """Test water boiling point conversion."""
        result = fahrenheit_to_celsius(212)
        assert abs(result - 100.0) < 0.01
    
    def test_fahrenheit_to_celsius_negative(self):
        """Test negative temperature conversion."""
        result = fahrenheit_to_celsius(-40)
        assert abs(result - (-40.0)) < 0.01


class TestDistanceConversions:
    """Test distance conversion functions."""
    
    def test_kilometers_to_miles_zero(self):
        """Test zero distance conversion."""
        assert kilometers_to_miles(0) == 0.0
    
    def test_kilometers_to_miles_positive(self):
        """Test positive distance conversion."""
        result = kilometers_to_miles(10)
        assert abs(result - 6.21371) < 0.01
    
    def test_miles_to_kilometers_zero(self):
        """Test zero distance conversion."""
        assert miles_to_kilometers(0) == 0.0
    
    def test_miles_to_kilometers_positive(self):
        """Test positive distance conversion."""
        result = miles_to_kilometers(10)
        assert abs(result - 16.0934) < 0.01


class TestWeightConversions:
    """Test weight conversion functions."""
    
    def test_kilograms_to_pounds_zero(self):
        """Test zero weight conversion."""
        assert kilograms_to_pounds(0) == 0.0
    
    def test_kilograms_to_pounds_positive(self):
        """Test positive weight conversion."""
        result = kilograms_to_pounds(10)
        assert abs(result - 22.0462) < 0.01
    
    def test_pounds_to_kilograms_zero(self):
        """Test zero weight conversion."""
        assert pounds_to_kilograms(0) == 0.0
    
    def test_pounds_to_kilograms_positive(self):
        """Test positive weight conversion."""
        result = pounds_to_kilograms(10)
        assert abs(result - 4.53592) < 0.01


class TestLengthConversions:
    """Test length conversion functions."""
    
    def test_centimeters_to_inches_zero(self):
        """Test zero length conversion."""
        assert centimeters_to_inches(0) == 0.0
    
    def test_centimeters_to_inches_positive(self):
        """Test positive length conversion."""
        result = centimeters_to_inches(10)
        assert abs(result - 3.93701) < 0.01
    
    def test_inches_to_centimeters_zero(self):
        """Test zero length conversion."""
        assert inches_to_centimeters(0) == 0.0
    
    def test_inches_to_centimeters_positive(self):
        """Test positive length conversion."""
        result = inches_to_centimeters(10)
        assert abs(result - 25.4) < 0.01


class TestRoundTripConversions:
    """Test that converting back and forth returns original value."""
    
    def test_temperature_round_trip(self):
        """Test Celsius → Fahrenheit → Celsius."""
        original = 25.0
        converted = celsius_to_fahrenheit(original)
        back = fahrenheit_to_celsius(converted)
        assert abs(back - original) < 0.01
    
    def test_distance_round_trip(self):
        """Test Kilometers → Miles → Kilometers."""
        original = 100.0
        converted = kilometers_to_miles(original)
        back = miles_to_kilometers(converted)
        assert abs(back - original) < 0.01
    
    def test_weight_round_trip(self):
        """Test Kilograms → Pounds → Kilograms."""
        original = 50.0
        converted = kilograms_to_pounds(original)
        back = pounds_to_kilograms(converted)
        assert abs(back - original) < 0.01
    
    def test_length_round_trip(self):
        """Test Centimeters → Inches → Centimeters."""
        original = 100.0
        converted = centimeters_to_inches(original)
        back = inches_to_centimeters(converted)
        assert abs(back - original) < 0.01
