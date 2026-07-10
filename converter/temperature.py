"""Temperature conversion functions."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        Temperature in Fahrenheit
        
    Raises:
        ValueError: If input is not a valid number
        TypeError: If input is not numeric
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number")
    
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in Fahrenheit
        
    Returns:
        Temperature in Celsius
        
    Raises:
        ValueError: If input is not a valid number
        TypeError: If input is not numeric
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Input must be a number")
    
    return (fahrenheit - 32) * 5/9