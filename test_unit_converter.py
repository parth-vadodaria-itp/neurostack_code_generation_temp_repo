"""Unit tests for the Unit Converter Application."""

import unittest
from unit_converter import UnitConverter


class TestUnitConverter(unittest.TestCase):
    """Test cases for UnitConverter class."""

    def setUp(self):
        """Set up test fixtures."""
        self.converter = UnitConverter()
        self.delta = 0.01  # Acceptable floating point difference

    def test_celsius_to_fahrenheit(self):
        """Test Celsius to Fahrenheit conversion."""
        self.assertAlmostEqual(
            self.converter.celsius_to_fahrenheit(0),
            32.0,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.celsius_to_fahrenheit(100),
            212.0,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.celsius_to_fahrenheit(-40),
            -40.0,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.celsius_to_fahrenheit(37),
            98.6,
            delta=self.delta
        )

    def test_fahrenheit_to_celsius(self):
        """Test Fahrenheit to Celsius conversion."""
        self.assertAlmostEqual(
            self.converter.fahrenheit_to_celsius(32),
            0.0,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.fahrenheit_to_celsius(212),
            100.0,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.fahrenheit_to_celsius(-40),
            -40.0,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.fahrenheit_to_celsius(98.6),
            37.0,
            delta=self.delta
        )

    def test_kilometers_to_miles(self):
        """Test Kilometers to Miles conversion."""
        self.assertAlmostEqual(
            self.converter.kilometers_to_miles(1),
            0.621371,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.kilometers_to_miles(10),
            6.21371,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.kilometers_to_miles(0),
            0.0,
            delta=self.delta
        )

    def test_miles_to_kilometers(self):
        """Test Miles to Kilometers conversion."""
        self.assertAlmostEqual(
            self.converter.miles_to_kilometers(1),
            1.60934,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.miles_to_kilometers(10),
            16.0934,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.miles_to_kilometers(0),
            0.0,
            delta=self.delta
        )

    def test_kilograms_to_pounds(self):
        """Test Kilograms to Pounds conversion."""
        self.assertAlmostEqual(
            self.converter.kilograms_to_pounds(1),
            2.20462,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.kilograms_to_pounds(10),
            22.0462,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.kilograms_to_pounds(0),
            0.0,
            delta=self.delta
        )

    def test_pounds_to_kilograms(self):
        """Test Pounds to Kilograms conversion."""
        self.assertAlmostEqual(
            self.converter.pounds_to_kilograms(1),
            0.453592,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.pounds_to_kilograms(10),
            4.53592,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.pounds_to_kilograms(0),
            0.0,
            delta=self.delta
        )

    def test_centimeters_to_inches(self):
        """Test Centimeters to Inches conversion."""
        self.assertAlmostEqual(
            self.converter.centimeters_to_inches(1),
            0.393701,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.centimeters_to_inches(10),
            3.93701,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.centimeters_to_inches(0),
            0.0,
            delta=self.delta
        )

    def test_inches_to_centimeters(self):
        """Test Inches to Centimeters conversion."""
        self.assertAlmostEqual(
            self.converter.inches_to_centimeters(1),
            2.54,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.inches_to_centimeters(10),
            25.4,
            delta=self.delta
        )
        self.assertAlmostEqual(
            self.converter.inches_to_centimeters(0),
            0.0,
            delta=self.delta
        )

    def test_temperature_round_trip(self):
        """Test round-trip temperature conversion."""
        celsius = 25.0
        fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
        back_to_celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
        self.assertAlmostEqual(celsius, back_to_celsius, delta=self.delta)

    def test_distance_round_trip(self):
        """Test round-trip distance conversion."""
        kilometers = 100.0
        miles = self.converter.kilometers_to_miles(kilometers)
        back_to_km = self.converter.miles_to_kilometers(miles)
        self.assertAlmostEqual(kilometers, back_to_km, delta=self.delta)

    def test_weight_round_trip(self):
        """Test round-trip weight conversion."""
        kilograms = 50.0
        pounds = self.converter.kilograms_to_pounds(kilograms)
        back_to_kg = self.converter.pounds_to_kilograms(pounds)
        self.assertAlmostEqual(kilograms, back_to_kg, delta=self.delta)

    def test_length_round_trip(self):
        """Test round-trip length conversion."""
        centimeters = 100.0
        inches = self.converter.centimeters_to_inches(centimeters)
        back_to_cm = self.converter.inches_to_centimeters(inches)
        self.assertAlmostEqual(centimeters, back_to_cm, delta=self.delta)


if __name__ == '__main__':
    unittest.main()
