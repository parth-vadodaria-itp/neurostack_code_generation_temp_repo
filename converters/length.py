"""Length conversion functions for Centimeters and Inches."""


def centimeters_to_inches(centimeters: float) -> float:
    """Convert Centimeters to Inches.
    
    Args:
        centimeters: Length in centimeters
        
    Returns:
        Length in inches
        
    Raises:
        TypeError: If centimeters is not a number
        ValueError: If centimeters is negative
    """
    if not isinstance(centimeters, (int, float)):
        raise TypeError("Length must be a number")
    
    if centimeters < 0:
        raise ValueError("Length cannot be negative")
    
    return centimeters * 0.393701


def inches_to_centimeters(inches: float) -> float:
    """Convert Inches to Centimeters.
    
    Args:
        inches: Length in inches
        
    Returns:
        Length in centimeters
        
    Raises:
        TypeError: If inches is not a number
        ValueError: If inches is negative
    """
    if not isinstance(inches, (int, float)):
        raise TypeError("Length must be a number")
    
    if inches < 0:
        raise ValueError("Length cannot be negative")
    
    return inches * 2.54