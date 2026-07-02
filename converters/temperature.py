"""Temperature conversion functions"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        Temperature in Fahrenheit
        
    Raises:
        ValueError: If celsius is below absolute zero (-273.15°C)
    """
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C)")
    
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius
    
    Args:
        fahrenheit: Temperature in Fahrenheit
        
    Returns:
        Temperature in Celsius
        
    Raises:
        ValueError: If fahrenheit is below absolute zero (-459.67°F)
    """
    if fahrenheit < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F)")
    
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)