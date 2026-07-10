"""Command-line interface for the Unit Converter application."""

import sys
from typing import Optional
from unit_converter.converter import UnitConverter
from unit_converter.validator import InputValidator


class CLI:
    """Command-line interface handler for unit conversion."""

    def __init__(self):
        """Initialize CLI with converter and validator."""
        self.converter = UnitConverter()
        self.validator = InputValidator()

    def display_menu(self) -> None:
        """Display the main menu with all available conversion options."""
        print("\n" + "=" * 50)
        print("        UNIT CONVERTER APPLICATION")
        print("=" * 50)
        print("\nAvailable Conversions:\n")

        conversions = self.converter.get_available_conversions()
        option_number = 1
        self.conversion_map = {}

        for category, conversion_types in conversions.items():
            print(f"\n{category.upper()}:")
            for conversion_type in conversion_types:
                display_name = conversion_type.replace("_", " ").title()
                print(f"  {option_number}. {display_name}")
                self.conversion_map[option_number] = (category, conversion_type)
                option_number += 1

        print(f"\n  {option_number}. Exit")
        print("\n" + "=" * 50)

    def get_user_choice(self) -> Optional[int]:
        """Get and validate user's menu choice.
        
        Returns:
            Valid menu choice number or None if invalid
        """
        try:
            choice = input("\nEnter your choice (number): ").strip()
            choice_num = int(choice)

            max_option = len(self.conversion_map) + 1
            if 1 <= choice_num <= max_option:
                return choice_num
            else:
                print(f"\n❌ Error: Please enter a number between 1 and {max_option}")
                return None
        except ValueError:
            print("\n❌ Error: Please enter a valid number")
            return None

    def get_value_input(self) -> Optional[float]:
        """Get and validate numeric value from user.
        
        Returns:
            Valid numeric value or None if invalid
        """
        try:
            value_str = input("Enter the value to convert: ").strip()
            value = float(value_str)

            if not self.validator.is_valid_number(value):
                print("\n❌ Error: Please enter a valid positive or negative number")
                return None

            return value
        except ValueError:
            print("\n❌ Error: Please enter a valid numeric value")
            return None

    def perform_conversion(self, category: str, conversion_type: str, value: float) -> None:
        """Execute the conversion and display the result.
        
        Args:
            category: Conversion category
            conversion_type: Specific conversion type
            value: Value to convert
        """
        try:
            result = self.converter.convert(category, conversion_type, value)

            from_unit, to_unit = conversion_type.split("_to_")
            from_unit = from_unit.replace("_", " ").title()
            to_unit = to_unit.replace("_", " ").title()

            print("\n" + "=" * 50)
            print("CONVERSION RESULT")
            print("=" * 50)
            print(f"\n  {value:.4f} {from_unit} = {result:.4f} {to_unit}")
            print("\n" + "=" * 50)
        except ValueError as e:
            print(f"\n❌ Conversion Error: {e}")

    def run(self) -> None:
        """Main application loop."""
        print("\nWelcome to the Unit Converter Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice is None:
                continue

            if choice == len(self.conversion_map) + 1:
                print("\nThank you for using Unit Converter. Goodbye!\n")
                sys.exit(0)

            category, conversion_type = self.conversion_map[choice]
            value = self.get_value_input()

            if value is None:
                continue

            self.perform_conversion(category, conversion_type, value)

            input("\nPress Enter to continue...")


def main():
    """Entry point for the CLI application."""
    try:
        cli = CLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
