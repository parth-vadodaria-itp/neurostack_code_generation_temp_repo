#!/usr/bin/env python3
"""
Unit Converter CLI Application
Supports temperature, distance, weight, and length conversions.
"""

import sys
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
from validators import validate_numeric_input, validate_menu_choice


def display_menu():
    """Display the main conversion menu."""
    print("\n" + "="*50)
    print("       UNIT CONVERTER APPLICATION")
    print("="*50)
    print("\nSelect a conversion type:")
    print("  1. Celsius → Fahrenheit")
    print("  2. Fahrenheit → Celsius")
    print("  3. Kilometers → Miles")
    print("  4. Miles → Kilometers")
    print("  5. Kilograms → Pounds")
    print("  6. Pounds → Kilograms")
    print("  7. Centimeters → Inches")
    print("  8. Inches → Centimeters")
    print("  9. Exit")
    print("="*50)


def get_conversion_input(unit_name):
    """
    Prompt user for numeric input with validation.
    
    Args:
        unit_name: Name of the unit being converted from
        
    Returns:
        float: Validated numeric value
    """
    while True:
        try:
            user_input = input(f"\nEnter value in {unit_name}: ").strip()
            value = validate_numeric_input(user_input)
            return value
        except ValueError as e:
            print(f"Error: {e}")
            print("Please enter a valid number.")


def perform_conversion(choice):
    """
    Execute the selected conversion.
    
    Args:
        choice: Menu option selected by user (1-8)
    """
    conversions_map = {
        1: ("Celsius", "Fahrenheit", celsius_to_fahrenheit),
        2: ("Fahrenheit", "Celsius", fahrenheit_to_celsius),
        3: ("Kilometers", "Miles", kilometers_to_miles),
        4: ("Miles", "Kilometers", miles_to_kilometers),
        5: ("Kilograms", "Pounds", kilograms_to_pounds),
        6: ("Pounds", "Kilograms", pounds_to_kilograms),
        7: ("Centimeters", "Inches", centimeters_to_inches),
        8: ("Inches", "Centimeters", inches_to_centimeters)
    }
    
    from_unit, to_unit, conversion_func = conversions_map[choice]
    
    value = get_conversion_input(from_unit)
    result = conversion_func(value)
    
    print("\n" + "-"*50)
    print(f"  {value:.2f} {from_unit} = {result:.2f} {to_unit}")
    print("-"*50)


def main():
    """Main application loop."""
    print("\nWelcome to the Unit Converter!")
    
    while True:
        display_menu()
        
        try:
            choice_input = input("\nEnter your choice (1-9): ").strip()
            choice = validate_menu_choice(choice_input, min_value=1, max_value=9)
            
            if choice == 9:
                print("\nThank you for using Unit Converter. Goodbye!")
                sys.exit(0)
            
            perform_conversion(choice)
            
        except ValueError as e:
            print(f"\nError: {e}")
            print("Please select a valid option from the menu.")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
