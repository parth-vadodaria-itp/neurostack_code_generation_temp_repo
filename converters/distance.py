"""Distance conversion functions"""


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles
    
    Args:
        kilometers: Distance in kilometers
        
    Returns:
        Distance in miles
        
    Raises:
        ValueError: If kilometers is negative
    """
    if kilometers < 0:
        raise ValueError("Distance cannot be negative")
    
    miles = kilometers * 0.621371
    return round(miles, 2)


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers
    
    Args:
        miles: Distance in miles
        
    Returns:
        Distance in kilometers
        
    Raises:
        ValueError: If miles is negative
    """
    if miles < 0:
        raise ValueError("Distance cannot be negative")
    
    kilometers = miles * 1.60934
    return round(kilometers, 2)