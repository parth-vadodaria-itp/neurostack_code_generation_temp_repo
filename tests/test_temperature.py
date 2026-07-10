"""Unit tests for temperature conversion functions."""

import pytest
from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestCelsiusToFahrenheit:
    """Test cases for celsius_to_fahrenheit function."""
    
    def test_freezing_point(self):
        """Test conversion of water freezing point."""
        assert celsius_to_fahrenheit(0) == 32.0
    
    def test_boiling_point(self):
        """Test conversion of water boiling point."""
        assert celsius_to_fahrenheit(100) == 212.0
    
    def test_negative_temperature(self):
        """Test conversion of negative temperature."""
        assert celsius_to_fahrenheit(-40) == -40.0
    
    def test_room_temperature(self):
        """Test conversion of typical room temperature."""
        result = celsius_to_fahrenheit(25)
        assert abs(result - 77.0) < 0.01
    
    def test_type_error(self):
        """Test that non-numeric input raises TypeError."""
        with pytest.raises(TypeError):
            celsius_to_fahrenheit("not a number")
    
    def test_below_absolute_zero(self):
        """Test that temperature below absolute zero raises ValueError."""
        with pytest.raises(ValueError):
            celsius_to_fahrenheit(-300)


class TestFahrenheitToCelsius:
    """Test cases for fahrenheit_to_celsius function."""
    
    def test_freezing_point(self):
        """Test conversion of water freezing point."""
        assert fahrenheit_to_celsius(32) == 0.0
    
    def test_boiling_point(self):
        """Test conversion of water boiling point."""
        assert fahrenheit_to_celsius(212) == 100.0
    
    def test_negative_temperature(self):
        """Test conversion of negative temperature."""
        assert fahrenheit_to_celsius(-40) == -40.0
    
    def test_room_temperature(self):
        """Test conversion of typical room temperature."""
        result = fahrenheit_to_celsius(77)
        assert abs(result - 25.0) < 0.01
    
    def test_type_error(self):
        """Test that non-numeric input raises TypeError."""
        with pytest.raises(TypeError):
            fahrenheit_to_celsius("not a number")
    
    def test_below_absolute_zero(self):
        """Test that temperature below absolute zero raises ValueError."""
        with pytest.raises(ValueError):
            fahrenheit_to_celsius(-500)