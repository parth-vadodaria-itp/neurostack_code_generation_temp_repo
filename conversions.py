"""
Conversion functions for temperature, distance, weight, and length units.
All functions accept numeric input and return float results.
"""


def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    Formula: F = (C × 9/5) + 32
    
    Args:
        celsius: Temperature in Celsius
        
    Returns:
        float: Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    Formula: C = (F - 32) × 5/9
    
    Args:
        fahrenheit: Temperature in Fahrenheit
        
    Returns:
        float: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def kilometers_to_miles(kilometers):
    """
    Convert kilometers to miles.
    
    Formula: miles = km × 0.621371
    
    Args:
        kilometers: Distance in kilometers
        
    Returns:
        float: Distance in miles
    """
    return kilometers * 0.621371


def miles_to_kilometers(miles):
    """
    Convert miles to kilometers.
    
    Formula: km = miles × 1.60934
    
    Args:
        miles: Distance in miles
        
    Returns:
        float: Distance in kilometers
    """
    return miles * 1.60934


def kilograms_to_pounds(kilograms):
    """
    Convert kilograms to pounds.
    
    Formula: lbs = kg × 2.20462
    
    Args:
        kilograms: Weight in kilograms
        
    Returns:
        float: Weight in pounds
    """
    return kilograms * 2.20462


def pounds_to_kilograms(pounds):
    """
    Convert pounds to kilograms.
    
    Formula: kg = lbs × 0.453592
    
    Args:
        pounds: Weight in pounds
        
    Returns:
        float: Weight in kilograms
    """
    return pounds * 0.453592


def centimeters_to_inches(centimeters):
    """
    Convert centimeters to inches.
    
    Formula: inches = cm × 0.393701
    
    Args:
        centimeters: Length in centimeters
        
    Returns:
        float: Length in inches
    """
    return centimeters * 0.393701


def inches_to_centimeters(inches):
    """
    Convert inches to centimeters.
    
    Formula: cm = inches × 2.54
    
    Args:
        inches: Length in inches
        
    Returns:
        float: Length in centimeters
    """
    return inches * 2.54
