#!/usr/bin/env python3
"""Unit Converter Application - Main Entry Point"""

from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converters.distance import kilometers_to_miles, miles_to_kilometers
from converters.weight import kilograms_to_pounds, pounds_to_kilograms
from converters.length import centimeters_to_inches, inches_to_centimeters
from validators.input_validator import validate_numeric_input, validate_menu_choice


def display_menu():
    """Display the conversion menu options."""
    print("\n=== Unit Converter Application ===")
    print("\nAvailable conversion types:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Centimeters to Inches")
    print("8. Inches to Centimeters")
    print("9. Exit")


def get_conversion_input(prompt="Enter value to convert: "):
    """Get and validate numeric input from user.
    
    Args:
        prompt: The prompt message to display
        
    Returns:
        float: The validated numeric input
        
    Raises:
        ValueError: If input is not a valid number
    """
    user_input = input(prompt)
    return validate_numeric_input(user_input)


def perform_conversion(choice, value):
    """Perform the selected conversion.
    
    Args:
        choice: The menu choice (1-8)
        value: The numeric value to convert
        
    Returns:
        tuple: (result, from_unit, to_unit)
    """
    conversions = {
        1: (celsius_to_fahrenheit, "Celsius", "Fahrenheit"),
        2: (fahrenheit_to_celsius, "Fahrenheit", "Celsius"),
        3: (kilometers_to_miles, "Kilometers", "Miles"),
        4: (miles_to_kilometers, "Miles", "Kilometers"),
        5: (kilograms_to_pounds, "Kilograms", "Pounds"),
        6: (pounds_to_kilograms, "Pounds", "Kilograms"),
        7: (centimeters_to_inches, "Centimeters", "Inches"),
        8: (inches_to_centimeters, "Inches", "Centimeters"),
    }
    
    converter_func, from_unit, to_unit = conversions[choice]
    result = converter_func(value)
    return result, from_unit, to_unit


def main():
    """Main application loop."""
    while True:
        try:
            display_menu()
            choice_input = input("\nSelect conversion type (1-9): ")
            choice = validate_menu_choice(choice_input, min_value=1, max_value=9)
            
            if choice == 9:
                print("\nThank you for using Unit Converter. Goodbye!")
                break
            
            value = get_conversion_input()
            result, from_unit, to_unit = perform_conversion(choice, value)
            
            print(f"\n{value} {from_unit} = {result} {to_unit}")
            
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please try again.")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
