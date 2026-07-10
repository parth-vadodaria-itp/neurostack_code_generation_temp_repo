"""Command-line interface for the unit converter."""

import sys
from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
    kilograms_to_pounds,
    pounds_to_kilograms,
    centimeters_to_inches,
    inches_to_centimeters,
)


CONVERSION_MENU = """
╔════════════════════════════════════════╗
║      UNIT CONVERTER APPLICATION        ║
╠════════════════════════════════════════╣
║  1. Celsius → Fahrenheit               ║
║  2. Fahrenheit → Celsius               ║
║  3. Kilometers → Miles                 ║
║  4. Miles → Kilometers                 ║
║  5. Kilograms → Pounds                 ║
║  6. Pounds → Kilograms                 ║
║  7. Centimeters → Inches               ║
║  8. Inches → Centimeters               ║
║  0. Exit                               ║
╚════════════════════════════════════════╝
"""


CONVERSION_MAP = {
    '1': {
        'name': 'Celsius to Fahrenheit',
        'func': celsius_to_fahrenheit,
        'input_unit': '°C',
        'output_unit': '°F',
        'prompt': 'Enter temperature in Celsius',
    },
    '2': {
        'name': 'Fahrenheit to Celsius',
        'func': fahrenheit_to_celsius,
        'input_unit': '°F',
        'output_unit': '°C',
        'prompt': 'Enter temperature in Fahrenheit',
    },
    '3': {
        'name': 'Kilometers to Miles',
        'func': kilometers_to_miles,
        'input_unit': 'km',
        'output_unit': 'miles',
        'prompt': 'Enter distance in kilometers',
    },
    '4': {
        'name': 'Miles to Kilometers',
        'func': miles_to_kilometers,
        'input_unit': 'miles',
        'output_unit': 'km',
        'prompt': 'Enter distance in miles',
    },
    '5': {
        'name': 'Kilograms to Pounds',
        'func': kilograms_to_pounds,
        'input_unit': 'kg',
        'output_unit': 'lbs',
        'prompt': 'Enter weight in kilograms',
    },
    '6': {
        'name': 'Pounds to Kilograms',
        'func': pounds_to_kilograms,
        'input_unit': 'lbs',
        'output_unit': 'kg',
        'prompt': 'Enter weight in pounds',
    },
    '7': {
        'name': 'Centimeters to Inches',
        'func': centimeters_to_inches,
        'input_unit': 'cm',
        'output_unit': 'in',
        'prompt': 'Enter length in centimeters',
    },
    '8': {
        'name': 'Inches to Centimeters',
        'func': inches_to_centimeters,
        'input_unit': 'in',
        'output_unit': 'cm',
        'prompt': 'Enter length in inches',
    },
}


def get_numeric_input(prompt: str) -> float:
    """Get and validate numeric input from user.
    
    Args:
        prompt: Input prompt message
        
    Returns:
        Validated numeric value
        
    Raises:
        ValueError: If input cannot be converted to float
    """
    while True:
        try:
            value = input(f"{prompt}: ").strip()
            return float(value)
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")


def perform_conversion(choice: str) -> None:
    """Perform the selected conversion.
    
    Args:
        choice: User's menu choice
    """
    if choice not in CONVERSION_MAP:
        print("❌ Invalid choice! Please select a valid option.\n")
        return
    
    conversion = CONVERSION_MAP[choice]
    print(f"\n{'='*50}")
    print(f"  {conversion['name']}")
    print(f"{'='*50}\n")
    
    try:
        value = get_numeric_input(conversion['prompt'])
        result = conversion['func'](value)
        
        print(f"\n✅ Result: {value:.2f} {conversion['input_unit']} = {result:.2f} {conversion['output_unit']}\n")
    except (ValueError, TypeError) as e:
        print(f"\n❌ Error: {str(e)}\n")


def run_cli() -> None:
    """Run the command-line interface."""
    print("\n" + "="*50)
    print("  Welcome to Unit Converter!")
    print("="*50)
    
    while True:
        print(CONVERSION_MENU)
        choice = input("Select conversion type (0-8): ").strip()
        
        if choice == '0':
            print("\n👋 Thank you for using Unit Converter! Goodbye.\n")
            sys.exit(0)
        
        perform_conversion(choice)
        
        input("Press Enter to continue...")
        print("\n" * 2)


if __name__ == '__main__':
    try:
        run_cli()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!\n")
        sys.exit(0)