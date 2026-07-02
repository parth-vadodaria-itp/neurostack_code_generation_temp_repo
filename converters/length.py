"""Length conversion functions"""


def centimeters_to_inches(centimeters: float) -> float:
    """Convert centimeters to inches
    
    Args:
        centimeters: Length in centimeters
        
    Returns:
        Length in inches
        
    Raises:
        ValueError: If centimeters is negative
    """
    if centimeters < 0:
        raise ValueError("Length cannot be negative")
    
    inches = centimeters * 0.393701
    return round(inches, 2)


def inches_to_centimeters(inches: float) -> float:
    """Convert inches to centimeters
    
    Args:
        inches: Length in inches
        
    Returns:
        Length in centimeters
        
    Raises:
        ValueError: If inches is negative
    """
    if inches < 0:
        raise ValueError("Length cannot be negative")
    
    centimeters = inches * 2.54
    return round(centimeters, 2)