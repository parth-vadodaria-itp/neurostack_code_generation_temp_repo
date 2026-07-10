"""Temperature conversion functions for Celsius and Fahrenheit."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        Temperature in Fahrenheit
        
    Raises:
        TypeError: If celsius is not a number
        ValueError: If celsius is below absolute zero (-273.15°C)
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Temperature must be a number")
    
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
    
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in Fahrenheit
        
    Returns:
        Temperature in Celsius
        
    Raises:
        TypeError: If fahrenheit is not a number
        ValueError: If fahrenheit is below absolute zero (-459.67°F)
    """
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Temperature must be a number")
    
    if fahrenheit < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
    
    return (fahrenheit - 32) * 5/9