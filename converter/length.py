"""Length conversion functions."""


def centimeters_to_inches(centimeters: float) -> float:
    """Convert centimeters to inches.
    
    Args:
        centimeters: Length in centimeters
        
    Returns:
        Length in inches
        
    Raises:
        ValueError: If input is negative
        TypeError: If input is not numeric
    """
    if not isinstance(centimeters, (int, float)):
        raise TypeError("Input must be a number")
    
    if centimeters < 0:
        raise ValueError("Length cannot be negative")
    
    return centimeters * 0.393701


def inches_to_centimeters(inches: float) -> float:
    """Convert inches to centimeters.
    
    Args:
        inches: Length in inches
        
    Returns:
        Length in centimeters
        
    Raises:
        ValueError: If input is negative
        TypeError: If input is not numeric
    """
    if not isinstance(inches, (int, float)):
        raise TypeError("Input must be a number")
    
    if inches < 0:
        raise ValueError("Length cannot be negative")
    
    return inches * 2.54