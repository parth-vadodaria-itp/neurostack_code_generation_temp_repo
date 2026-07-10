"""Core conversion logic for the Unit Converter application."""

from typing import Dict, Callable


class UnitConverter:
    """Handles all unit conversion operations."""

    def __init__(self):
        """Initialize the converter with all supported conversion functions."""
        self.conversions: Dict[str, Dict[str, Callable[[float], float]]] = {
            "temperature": {
                "celsius_to_fahrenheit": self._celsius_to_fahrenheit,
                "fahrenheit_to_celsius": self._fahrenheit_to_celsius,
            },
            "distance": {
                "kilometers_to_miles": self._kilometers_to_miles,
                "miles_to_kilometers": self._miles_to_kilometers,
                "centimeters_to_inches": self._centimeters_to_inches,
                "inches_to_centimeters": self._inches_to_centimeters,
            },
            "weight": {
                "kilograms_to_pounds": self._kilograms_to_pounds,
                "pounds_to_kilograms": self._pounds_to_kilograms,
            },
        }

    @staticmethod
    def _celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit.
        
        Args:
            celsius: Temperature in Celsius
            
        Returns:
            Temperature in Fahrenheit
        """
        return (celsius * 9 / 5) + 32

    @staticmethod
    def _fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius.
        
        Args:
            fahrenheit: Temperature in Fahrenheit
            
        Returns:
            Temperature in Celsius
        """
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def _kilometers_to_miles(kilometers: float) -> float:
        """Convert kilometers to miles.
        
        Args:
            kilometers: Distance in kilometers
            
        Returns:
            Distance in miles
        """
        return kilometers * 0.621371

    @staticmethod
    def _miles_to_kilometers(miles: float) -> float:
        """Convert miles to kilometers.
        
        Args:
            miles: Distance in miles
            
        Returns:
            Distance in kilometers
        """
        return miles * 1.60934

    @staticmethod
    def _kilograms_to_pounds(kilograms: float) -> float:
        """Convert kilograms to pounds.
        
        Args:
            kilograms: Weight in kilograms
            
        Returns:
            Weight in pounds
        """
        return kilograms * 2.20462

    @staticmethod
    def _pounds_to_kilograms(pounds: float) -> float:
        """Convert pounds to kilograms.
        
        Args:
            pounds: Weight in pounds
            
        Returns:
            Weight in kilograms
        """
        return pounds * 0.453592

    @staticmethod
    def _centimeters_to_inches(centimeters: float) -> float:
        """Convert centimeters to inches.
        
        Args:
            centimeters: Length in centimeters
            
        Returns:
            Length in inches
        """
        return centimeters * 0.393701

    @staticmethod
    def _inches_to_centimeters(inches: float) -> float:
        """Convert inches to centimeters.
        
        Args:
            inches: Length in inches
            
        Returns:
            Length in centimeters
        """
        return inches * 2.54

    def convert(self, category: str, conversion_type: str, value: float) -> float:
        """Perform a unit conversion.
        
        Args:
            category: The category of conversion (temperature, distance, weight)
            conversion_type: The specific conversion to perform
            value: The value to convert
            
        Returns:
            The converted value
            
        Raises:
            ValueError: If category or conversion_type is invalid
        """
        if category not in self.conversions:
            raise ValueError(
                f"Invalid category '{category}'. "
                f"Valid categories: {', '.join(self.conversions.keys())}"
            )

        if conversion_type not in self.conversions[category]:
            raise ValueError(
                f"Invalid conversion type '{conversion_type}' for category '{category}'. "
                f"Valid types: {', '.join(self.conversions[category].keys())}"
            )

        conversion_func = self.conversions[category][conversion_type]
        return conversion_func(value)

    def get_available_conversions(self) -> Dict[str, list]:
        """Get all available conversion types organized by category.
        
        Returns:
            Dictionary mapping categories to lists of conversion types
        """
        return {category: list(conversions.keys()) for category, conversions in self.conversions.items()}
