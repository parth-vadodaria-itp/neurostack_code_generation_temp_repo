#!/usr/bin/env python3
"""Unit Converter Application - Main Entry Point"""

from ui.menu import display_menu, get_user_choice, get_value_input
from validators.input_validator import validate_numeric_input
from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converters.distance import kilometers_to_miles, miles_to_kilometers
from converters.weight import kilograms_to_pounds, pounds_to_kilograms
from converters.length import centimeters_to_inches, inches_to_centimeters


def main():
    """Main application loop"""
    print("=== Unit Converter Application ===")
    print()
    
    conversion_map = {
        1: ("Celsius", "Fahrenheit", celsius_to_fahrenheit),
        2: ("Fahrenheit", "Celsius", fahrenheit_to_celsius),
        3: ("Kilometers", "Miles", kilometers_to_miles),
        4: ("Miles", "Kilometers", miles_to_kilometers),
        5: ("Kilograms", "Pounds", kilograms_to_pounds),
        6: ("Pounds", "Kilograms", pounds_to_kilograms),
        7: ("Centimeters", "Inches", centimeters_to_inches),
        8: ("Inches", "Centimeters", inches_to_centimeters),
    }
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 9:
            print("\nThank you for using Unit Converter!")
            break
        
        if choice not in conversion_map:
            print("\nInvalid selection. Please try again.\n")
            continue
        
        from_unit, to_unit, converter_func = conversion_map[choice]
        
        value_str = get_value_input()
        
        is_valid, value, error_message = validate_numeric_input(value_str)
        
        if not is_valid:
            print(f"\nError: {error_message}\n")
            continue
        
        try:
            result = converter_func(value)
            print(f"\n{value} {from_unit} = {result} {to_unit}\n")
        except ValueError as e:
            print(f"\nError: {str(e)}\n")
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}\n")


if __name__ == "__main__":
    main()