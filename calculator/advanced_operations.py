"""Advanced mathematical operations: modulo, square, square root."""

import math


class AdvancedCalculator:
    """Handles advanced mathematical operations."""

    @staticmethod
    def modulo(a: float, b: float) -> float:
        """Calculate modulo (remainder) of a divided by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero divisor")
        return a % b

    @staticmethod
    def square(a: float) -> float:
        """Calculate the square of a number.
        
        Args:
            a: Number to square
            
        Returns:
            Square of a (a²)
        """
        return a ** 2

    @staticmethod
    def square_root(a: float) -> float:
        """Calculate the square root of a number.
        
        Args:
            a: Number to find square root of
            
        Returns:
            Square root of a (√a)
            
        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
