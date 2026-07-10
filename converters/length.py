"""Length conversion functions."""


def centimeters_to_inches(centimeters: float) -> float:
    """Convert Centimeters to Inches.
    
    Formula: inches = centimeters × 0.393701
    
    Args:
        centimeters: Length in centimeters
        
    Returns:
        float: Length in inches
        
    Examples:
        >>> round(centimeters_to_inches(1), 2)
        0.39
        >>> round(centimeters_to_inches(10), 2)
        3.94
        >>> round(centimeters_to_inches(100), 2)
        39.37
    """
    return centimeters * 0.393701


def inches_to_centimeters(inches: float) -> float:
    """Convert Inches to Centimeters.
    
    Formula: centimeters = inches × 2.54
    
    Args:
        inches: Length in inches
        
    Returns:
        float: Length in centimeters
        
    Examples:
        >>> inches_to_centimeters(1)
        2.54
        >>> inches_to_centimeters(10)
        25.4
        >>> inches_to_centimeters(100)
        254.0
    """
    return inches * 2.54
