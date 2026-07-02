"""User interface and menu functions"""


def display_menu() -> None:
    """Display the conversion menu options"""
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Centimeters to Inches")
    print("8. Inches to Centimeters")
    print("9. Exit")
    print()


def get_user_choice() -> int:
    """Get and validate user's menu choice
    
    Returns:
        Integer choice (1-9), or 0 if invalid
    """
    try:
        choice = int(input("Select conversion type (1-9): "))
        return choice
    except ValueError:
        return 0


def get_value_input() -> str:
    """Get value to convert from user
    
    Returns:
        String input from user
    """
    return input("Enter value to convert: ")