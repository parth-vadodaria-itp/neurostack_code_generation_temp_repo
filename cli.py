#!/usr/bin/env python3
"""Command-line interface for the Unit Converter application."""

import sys
from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converters.distance import kilometers_to_miles, miles_to_kilometers
from converters.weight import kilograms_to_pounds, pounds_to_kilograms
from converters.length import centimeters_to_inches, inches_to_centimeters


def display_menu():
    """Display the conversion type menu."""
    print("\n" + "="*50)
    print("Unit Converter Application")
    print("="*50)
    print("\nSelect a conversion type:")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Kilometers → Miles")
    print("4. Miles → Kilometers")
    print("5. Kilograms → Pounds")
    print("6. Pounds → Kilograms")
    print("7. Centimeters → Inches")
    print("8. Inches → Centimeters")
    print("9. Exit")
    print("="*50)


def get_numeric_input(prompt: str) -> float:
    """Get and validate numeric input from user.
    
    Args:
        prompt: The prompt message to display
        
    Returns:
        The validated numeric input
        
    Raises:
        ValueError: If input is not a valid number
    """
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Error: Please enter a valid number.")


def perform_conversion(choice: int):
    """Perform the selected conversion.
    
    Args:
        choice: The menu choice (1-8)
    """
    conversions = {
        1: ("Celsius", "Fahrenheit", celsius_to_fahrenheit),
        2: ("Fahrenheit", "Celsius", fahrenheit_to_celsius),
        3: ("Kilometers", "Miles", kilometers_to_miles),
        4: ("Miles", "Kilometers", miles_to_kilometers),
        5: ("Kilograms", "Pounds", kilograms_to_pounds),
        6: ("Pounds", "Kilograms", pounds_to_kilograms),
        7: ("Centimeters", "Inches", centimeters_to_inches),
        8: ("Inches", "Centimeters", inches_to_centimeters),
    }
    
    if choice not in conversions:
        print("Error: Invalid choice. Please select 1-9.")
        return
    
    from_unit, to_unit, converter_func = conversions[choice]
    
    try:
        value = get_numeric_input(f"\nEnter value in {from_unit}: ")
        result = converter_func(value)
        print(f"\n✓ Result: {value:.2f} {from_unit} = {result:.2f} {to_unit}")
    except (ValueError, TypeError) as e:
        print(f"\n✗ Error: {str(e)}")


def main():
    """Main application loop."""
    print("\nWelcome to the Unit Converter Application!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-9): "))
            
            if choice == 9:
                print("\nThank you for using Unit Converter. Goodbye!")
                sys.exit(0)
            
            perform_conversion(choice)
            
            input("\nPress Enter to continue...")
            
        except ValueError:
            print("\nError: Please enter a number between 1 and 9.")
            input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
            sys.exit(0)


if __name__ == "__main__":
    main()