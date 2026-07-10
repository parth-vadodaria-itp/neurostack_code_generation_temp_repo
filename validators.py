"""
Input validation functions for the unit converter application.
Ensures user input is valid before processing conversions.
"""


def validate_numeric_input(value_str):
    """
    Validate that input string is a valid number.
    
    Args:
        value_str: String input from user
        
    Returns:
        float: Validated numeric value
        
    Raises:
        ValueError: If input is not a valid number
    """
    if not value_str:
        raise ValueError("Input cannot be empty")
    
    try:
        value = float(value_str)
        return value
    except ValueError:
        raise ValueError(f"'{value_str}' is not a valid number")


def validate_menu_choice(choice_str, min_value=1, max_value=9):
    """
    Validate menu choice is within valid range.
    
    Args:
        choice_str: String input from user
        min_value: Minimum valid choice (inclusive)
        max_value: Maximum valid choice (inclusive)
        
    Returns:
        int: Validated menu choice
        
    Raises:
        ValueError: If choice is not valid
    """
    if not choice_str:
        raise ValueError("Choice cannot be empty")
    
    try:
        choice = int(choice_str)
    except ValueError:
        raise ValueError(f"'{choice_str}' is not a valid menu option")
    
    if choice < min_value or choice > max_value:
        raise ValueError(
            f"Choice must be between {min_value} and {max_value}, got {choice}"
        )
    
    return choice
