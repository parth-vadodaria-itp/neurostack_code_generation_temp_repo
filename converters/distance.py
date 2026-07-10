"""Distance conversion functions for Kilometers and Miles."""


def kilometers_to_miles(kilometers: float) -> float:
    """Convert Kilometers to Miles.
    
    Args:
        kilometers: Distance in kilometers
        
    Returns:
        Distance in miles
        
    Raises:
        TypeError: If kilometers is not a number
        ValueError: If kilometers is negative
    """
    if not isinstance(kilometers, (int, float)):
        raise TypeError("Distance must be a number")
    
    if kilometers < 0:
        raise ValueError("Distance cannot be negative")
    
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    """Convert Miles to Kilometers.
    
    Args:
        miles: Distance in miles
        
    Returns:
        Distance in kilometers
        
    Raises:
        TypeError: If miles is not a number
        ValueError: If miles is negative
    """
    if not isinstance(miles, (int, float)):
        raise TypeError("Distance must be a number")
    
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    
    return miles * 1.60934