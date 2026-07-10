"""Temperature conversion functions."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.
    
    Formula: F = (C × 9/5) + 32
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
        
    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(25)
        77.0
    """
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) × 5/9
    
    Args:
        fahrenheit: Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
        
    Examples:
        >>> fahrenheit_to_celsius(32)
        0.0
        >>> fahrenheit_to_celsius(212)
        100.0
        >>> fahrenheit_to_celsius(77)
        25.0
    """
    return (fahrenheit - 32) * 5 / 9
