"""Weight conversion functions"""


def kilograms_to_pounds(kilograms: float) -> float:
    """Convert kilograms to pounds
    
    Args:
        kilograms: Weight in kilograms
        
    Returns:
        Weight in pounds
        
    Raises:
        ValueError: If kilograms is negative
    """
    if kilograms < 0:
        raise ValueError("Weight cannot be negative")
    
    pounds = kilograms * 2.20462
    return round(pounds, 2)


def pounds_to_kilograms(pounds: float) -> float:
    """Convert pounds to kilograms
    
    Args:
        pounds: Weight in pounds
        
    Returns:
        Weight in kilograms
        
    Raises:
        ValueError: If pounds is negative
    """
    if pounds < 0:
        raise ValueError("Weight cannot be negative")
    
    kilograms = pounds * 0.453592
    return round(kilograms, 2)