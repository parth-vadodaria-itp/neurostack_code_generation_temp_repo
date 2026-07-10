"""Weight conversion functions for Kilograms and Pounds."""


def kilograms_to_pounds(kilograms: float) -> float:
    """Convert Kilograms to Pounds.
    
    Args:
        kilograms: Weight in kilograms
        
    Returns:
        Weight in pounds
        
    Raises:
        TypeError: If kilograms is not a number
        ValueError: If kilograms is negative
    """
    if not isinstance(kilograms, (int, float)):
        raise TypeError("Weight must be a number")
    
    if kilograms < 0:
        raise ValueError("Weight cannot be negative")
    
    return kilograms * 2.20462


def pounds_to_kilograms(pounds: float) -> float:
    """Convert Pounds to Kilograms.
    
    Args:
        pounds: Weight in pounds
        
    Returns:
        Weight in kilograms
        
    Raises:
        TypeError: If pounds is not a number
        ValueError: If pounds is negative
    """
    if not isinstance(pounds, (int, float)):
        raise TypeError("Weight must be a number")
    
    if pounds < 0:
        raise ValueError("Weight cannot be negative")
    
    return pounds * 0.453592