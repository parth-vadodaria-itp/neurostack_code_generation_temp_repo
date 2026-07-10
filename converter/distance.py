"""Distance conversion functions."""


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles.
    
    Args:
        kilometers: Distance in kilometers
        
    Returns:
        Distance in miles
        
    Raises:
        ValueError: If input is negative
        TypeError: If input is not numeric
    """
    if not isinstance(kilometers, (int, float)):
        raise TypeError("Input must be a number")
    
    if kilometers < 0:
        raise ValueError("Distance cannot be negative")
    
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers.
    
    Args:
        miles: Distance in miles
        
    Returns:
        Distance in kilometers
        
    Raises:
        ValueError: If input is negative
        TypeError: If input is not numeric
    """
    if not isinstance(miles, (int, float)):
        raise TypeError("Input must be a number")
    
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    
    return miles * 1.60934