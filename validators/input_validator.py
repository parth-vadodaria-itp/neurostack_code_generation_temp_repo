"""Input validation functions for the unit converter application."""


def validate_numeric_input(value: str) -> float:
    """Validate that input is a valid numeric value.
    
    Args:
        value: String input from user
        
    Returns:
        float: The validated numeric value
        
    Raises:
        ValueError: If input is not a valid number
        
    Examples:
        >>> validate_numeric_input("42")
        42.0
        >>> validate_numeric_input("3.14")
        3.14
        >>> validate_numeric_input("-10")
        -10.0
    """
    if not value or value.strip() == "":
        raise ValueError("Input cannot be empty")
    
    try:
        numeric_value = float(value)
        return numeric_value
    except ValueError:
        raise ValueError(f"'{value}' is not a valid number")


def validate_menu_choice(choice: str, min_value: int = 1, max_value: int = 9) -> int:
    """Validate that menu choice is within valid range.
    
    Args:
        choice: String input from user
        min_value: Minimum valid choice (inclusive)
        max_value: Maximum valid choice (inclusive)
        
    Returns:
        int: The validated menu choice
        
    Raises:
        ValueError: If choice is not a valid integer or out of range
        
    Examples:
        >>> validate_menu_choice("1")
        1
        >>> validate_menu_choice("5", 1, 9)
        5
        >>> validate_menu_choice("9", 1, 9)
        9
    """
    if not choice or choice.strip() == "":
        raise ValueError("Choice cannot be empty")
    
    try:
        choice_int = int(choice)
    except ValueError:
        raise ValueError(f"'{choice}' is not a valid menu option")
    
    if choice_int < min_value or choice_int > max_value:
        raise ValueError(
            f"Choice must be between {min_value} and {max_value}, got {choice_int}"
        )
    
    return choice_int
