"""Weight conversion functions."""


def kilograms_to_pounds(kilograms: float) -> float:
    """Convert Kilograms to Pounds.
    
    Formula: pounds = kilograms × 2.20462
    
    Args:
        kilograms: Weight in kilograms
        
    Returns:
        float: Weight in pounds
        
    Examples:
        >>> round(kilograms_to_pounds(1), 2)
        2.2
        >>> round(kilograms_to_pounds(10), 2)
        22.05
        >>> round(kilograms_to_pounds(100), 2)
        220.46
    """
    return kilograms * 2.20462


def pounds_to_kilograms(pounds: float) -> float:
    """Convert Pounds to Kilograms.
    
    Formula: kilograms = pounds × 0.453592
    
    Args:
        pounds: Weight in pounds
        
    Returns:
        float: Weight in kilograms
        
    Examples:
        >>> round(pounds_to_kilograms(1), 2)
        0.45
        >>> round(pounds_to_kilograms(10), 2)
        4.54
        >>> round(pounds_to_kilograms(100), 2)
        45.36
    """
    return pounds * 0.453592
