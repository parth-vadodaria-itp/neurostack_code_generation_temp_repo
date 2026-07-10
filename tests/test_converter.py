"""Unit tests for the converter module."""

import pytest
from unit_converter.converter import UnitConverter


class TestUnitConverter:
    """Test cases for UnitConverter class."""

    @pytest.fixture
    def converter(self):
        """Create a UnitConverter instance for testing."""
        return UnitConverter()

    def test_celsius_to_fahrenheit(self, converter):
        """Test Celsius to Fahrenheit conversion."""
        result = converter.convert("temperature", "celsius_to_fahrenheit", 0)
        assert result == 32.0

        result = converter.convert("temperature", "celsius_to_fahrenheit", 100)
        assert result == 212.0

        result = converter.convert("temperature", "celsius_to_fahrenheit", -40)
        assert result == -40.0

    def test_fahrenheit_to_celsius(self, converter):
        """Test Fahrenheit to Celsius conversion."""
        result = converter.convert("temperature", "fahrenheit_to_celsius", 32)
        assert result == 0.0

        result = converter.convert("temperature", "fahrenheit_to_celsius", 212)
        assert result == 100.0

        result = converter.convert("temperature", "fahrenheit_to_celsius", -40)
        assert result == -40.0

    def test_kilometers_to_miles(self, converter):
        """Test kilometers to miles conversion."""
        result = converter.convert("distance", "kilometers_to_miles", 1)
        assert abs(result - 0.621371) < 0.0001

        result = converter.convert("distance", "kilometers_to_miles", 10)
        assert abs(result - 6.21371) < 0.0001

    def test_miles_to_kilometers(self, converter):
        """Test miles to kilometers conversion."""
        result = converter.convert("distance", "miles_to_kilometers", 1)
        assert abs(result - 1.60934) < 0.0001

        result = converter.convert("distance", "miles_to_kilometers", 10)
        assert abs(result - 16.0934) < 0.0001

    def test_kilograms_to_pounds(self, converter):
        """Test kilograms to pounds conversion."""
        result = converter.convert("weight", "kilograms_to_pounds", 1)
        assert abs(result - 2.20462) < 0.0001

        result = converter.convert("weight", "kilograms_to_pounds", 10)
        assert abs(result - 22.0462) < 0.0001

    def test_pounds_to_kilograms(self, converter):
        """Test pounds to kilograms conversion."""
        result = converter.convert("weight", "pounds_to_kilograms", 1)
        assert abs(result - 0.453592) < 0.0001

        result = converter.convert("weight", "pounds_to_kilograms", 10)
        assert abs(result - 4.53592) < 0.0001

    def test_centimeters_to_inches(self, converter):
        """Test centimeters to inches conversion."""
        result = converter.convert("distance", "centimeters_to_inches", 1)
        assert abs(result - 0.393701) < 0.0001

        result = converter.convert("distance", "centimeters_to_inches", 100)
        assert abs(result - 39.3701) < 0.0001

    def test_inches_to_centimeters(self, converter):
        """Test inches to centimeters conversion."""
        result = converter.convert("distance", "inches_to_centimeters", 1)
        assert abs(result - 2.54) < 0.0001

        result = converter.convert("distance", "inches_to_centimeters", 10)
        assert abs(result - 25.4) < 0.0001

    def test_invalid_category(self, converter):
        """Test that invalid category raises ValueError."""
        with pytest.raises(ValueError, match="Invalid category"):
            converter.convert("invalid_category", "some_conversion", 10)

    def test_invalid_conversion_type(self, converter):
        """Test that invalid conversion type raises ValueError."""
        with pytest.raises(ValueError, match="Invalid conversion type"):
            converter.convert("temperature", "invalid_conversion", 10)

    def test_get_available_conversions(self, converter):
        """Test retrieval of available conversions."""
        conversions = converter.get_available_conversions()

        assert "temperature" in conversions
        assert "distance" in conversions
        assert "weight" in conversions

        assert "celsius_to_fahrenheit" in conversions["temperature"]
        assert "fahrenheit_to_celsius" in conversions["temperature"]
        assert "kilometers_to_miles" in conversions["distance"]
        assert "miles_to_kilometers" in conversions["distance"]
        assert "kilograms_to_pounds" in conversions["weight"]
        assert "pounds_to_kilograms" in conversions["weight"]
