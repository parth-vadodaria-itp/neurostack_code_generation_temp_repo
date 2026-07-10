"""Weight conversion functions."""


def kilograms_to_pounds(kilograms: float) -> float:
    """Convert kilograms to pounds.
    
    Args:
        kilograms: Weight in kilograms
        
    Returns:
        Weight in pounds
        
    Raises:
        ValueError: If input is negative
        TypeError: If input is not numeric
    """
    if not isinstance(kilograms, (int, float)):
        raise TypeError("Input must be a number")
    
    if kilograms < 0:
        raise ValueError("Weight cannot be negative")
    
    return kilograms * 2.20462


def pounds_to_kilograms(pounds: float) -> float:
    """Convert pounds to kilograms.
    
    Args:
        pounds: Weight in pounds
        
    Returns:
        Weight in kilograms
        
    Raises:
        ValueError: If input is negative
        TypeError: If input is not numeric
    """
    if not isinstance(pounds, (int, float)):
        raise TypeError("Input must be a number")
    
    if pounds < 0:
        raise ValueError("Weight cannot be negative")
    
    return pounds * 0.453592