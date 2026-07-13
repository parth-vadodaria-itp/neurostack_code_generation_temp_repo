"""Unit Converter Application

A Python application for converting values between commonly used units.
Supports temperature, distance, weight, and length conversions.
"""

import sys
from typing import Tuple, Optional


class UnitConverter:
    """Main converter class handling all unit conversions."""

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit.
        
        Args:
            celsius: Temperature in Celsius
            
        Returns:
            Temperature in Fahrenheit
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius.
        
        Args:
            fahrenheit: Temperature in Fahrenheit
            
        Returns:
            Temperature in Celsius
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def kilometers_to_miles(kilometers: float) -> float:
        """Convert Kilometers to Miles.
        
        Args:
            kilometers: Distance in kilometers
            
        Returns:
            Distance in miles
        """
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles: float) -> float:
        """Convert Miles to Kilometers.
        
        Args:
            miles: Distance in miles
            
        Returns:
            Distance in kilometers
        """
        return miles * 1.60934

    @staticmethod
    def kilograms_to_pounds(kilograms: float) -> float:
        """Convert Kilograms to Pounds.
        
        Args:
            kilograms: Weight in kilograms
            
        Returns:
            Weight in pounds
        """
        return kilograms * 2.20462

    @staticmethod
    def pounds_to_kilograms(pounds: float) -> float:
        """Convert Pounds to Kilograms.
        
        Args:
            pounds: Weight in pounds
            
        Returns:
            Weight in kilograms
        """
        return pounds * 0.453592

    @staticmethod
    def centimeters_to_inches(centimeters: float) -> float:
        """Convert Centimeters to Inches.
        
        Args:
            centimeters: Length in centimeters
            
        Returns:
            Length in inches
        """
        return centimeters * 0.393701

    @staticmethod
    def inches_to_centimeters(inches: float) -> float:
        """Convert Inches to Centimeters.
        
        Args:
            inches: Length in inches
            
        Returns:
            Length in centimeters
        """
        return inches * 2.54


class ConverterUI:
    """User interface for the unit converter application."""

    CONVERSION_OPTIONS = {
        '1': ('Celsius to Fahrenheit', UnitConverter.celsius_to_fahrenheit, '°C', '°F'),
        '2': ('Fahrenheit to Celsius', UnitConverter.fahrenheit_to_celsius, '°F', '°C'),
        '3': ('Kilometers to Miles', UnitConverter.kilometers_to_miles, 'km', 'mi'),
        '4': ('Miles to Kilometers', UnitConverter.miles_to_kilometers, 'mi', 'km'),
        '5': ('Kilograms to Pounds', UnitConverter.kilograms_to_pounds, 'kg', 'lb'),
        '6': ('Pounds to Kilograms', UnitConverter.pounds_to_kilograms, 'lb', 'kg'),
        '7': ('Centimeters to Inches', UnitConverter.centimeters_to_inches, 'cm', 'in'),
        '8': ('Inches to Centimeters', UnitConverter.inches_to_centimeters, 'in', 'cm'),
    }

    def display_menu(self) -> None:
        """Display the conversion menu."""
        print("\n" + "="*50)
        print("Unit Converter Application")
        print("="*50)
        print("\nSelect a conversion type:")
        print()
        for key, (description, _, _, _) in self.CONVERSION_OPTIONS.items():
            print(f"{key}. {description}")
        print("0. Exit")
        print()

    def get_user_choice(self) -> Optional[str]:
        """Get and validate user's conversion choice.
        
        Returns:
            Valid choice or None to exit
        """
        while True:
            choice = input("Enter your choice (0-8): ").strip()
            
            if choice == '0':
                return None
            
            if choice in self.CONVERSION_OPTIONS:
                return choice
            
            print("❌ Invalid choice. Please enter a number between 0 and 8.")

    def get_numeric_input(self, prompt: str) -> Optional[float]:
        """Get and validate numeric input from user.
        
        Args:
            prompt: Input prompt message
            
        Returns:
            Valid numeric value or None if invalid
        """
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")
            return None

    def perform_conversion(self, choice: str) -> None:
        """Perform the selected conversion.
        
        Args:
            choice: User's conversion choice
        """
        description, converter_func, from_unit, to_unit = self.CONVERSION_OPTIONS[choice]
        
        print(f"\n{description}")
        print("-" * 40)
        
        value = self.get_numeric_input(f"Enter value in {from_unit}: ")
        
        if value is None:
            return
        
        result = converter_func(value)
        print(f"\n✓ Result: {value:.2f} {from_unit} = {result:.2f} {to_unit}")

    def run(self) -> None:
        """Run the main application loop."""
        print("\nWelcome to the Unit Converter Application!")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice is None:
                print("\nThank you for using Unit Converter. Goodbye!")
                break
            
            self.perform_conversion(choice)
            
            input("\nPress Enter to continue...")


def main() -> int:
    """Main entry point for the application.
    
    Returns:
        Exit code (0 for success)
    """
    try:
        app = ConverterUI()
        app.run()
        return 0
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Exiting...")
        return 130
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
