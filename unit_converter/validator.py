"""Input validation utilities for the Unit Converter application."""

import math
from typing import Union


class InputValidator:
    """Validates user input for unit conversion operations."""

    @staticmethod
    def is_valid_number(value: Union[int, float]) -> bool:
        """Check if a value is a valid number for conversion.
        
        Args:
            value: The value to validate
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(value, (int, float)):
            return False

        if math.isnan(value) or math.isinf(value):
            return False

        return True

    @staticmethod
    def is_positive_number(value: Union[int, float]) -> bool:
        """Check if a value is a positive number.
        
        Args:
            value: The value to validate
            
        Returns:
            True if positive, False otherwise
        """
        return InputValidator.is_valid_number(value) and value > 0

    @staticmethod
    def is_in_range(value: Union[int, float], min_val: float, max_val: float) -> bool:
        """Check if a value is within a specified range.
        
        Args:
            value: The value to check
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            True if in range, False otherwise
        """
        if not InputValidator.is_valid_number(value):
            return False

        return min_val <= value <= max_val
