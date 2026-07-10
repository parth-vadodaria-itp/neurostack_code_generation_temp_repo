"""Distance conversion functions."""


def kilometers_to_miles(kilometers: float) -> float:
    """Convert Kilometers to Miles.
    
    Formula: miles = kilometers × 0.621371
    
    Args:
        kilometers: Distance in kilometers
        
    Returns:
        float: Distance in miles
        
    Examples:
        >>> round(kilometers_to_miles(1), 2)
        0.62
        >>> round(kilometers_to_miles(10), 2)
        6.21
        >>> round(kilometers_to_miles(100), 2)
        62.14
    """
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    """Convert Miles to Kilometers.
    
    Formula: kilometers = miles × 1.60934
    
    Args:
        miles: Distance in miles
        
    Returns:
        float: Distance in kilometers
        
    Examples:
        >>> round(miles_to_kilometers(1), 2)
        1.61
        >>> round(miles_to_kilometers(10), 2)
        16.09
        >>> round(miles_to_kilometers(100), 2)
        160.93
    """
    return miles * 1.60934
