"""Input validation functions"""

from typing import Tuple, Optional


def validate_numeric_input(value_str: str) -> Tuple[bool, Optional[float], Optional[str]]:
    """Validate that input string is a valid numeric value
    
    Args:
        value_str: String input from user
        
    Returns:
        Tuple of (is_valid, parsed_value, error_message)
        - is_valid: True if input is valid, False otherwise
        - parsed_value: Float value if valid, None otherwise
        - error_message: Error description if invalid, None otherwise
    """
    if not value_str or value_str.strip() == "":
        return False, None, "Input cannot be empty"
    
    value_str = value_str.strip()
    
    try:
        value = float(value_str)
        return True, value, None
    except ValueError:
        return False, None, f"'{value_str}' is not a valid number"