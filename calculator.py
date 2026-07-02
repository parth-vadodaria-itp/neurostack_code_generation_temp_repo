"""
Calculator module providing basic and advanced mathematical operations.
"""
import math


class Calculator:
    """
    A calculator class that supports basic and advanced mathematical operations.
    
    Basic operations: addition, subtraction, multiplication, division
    Advanced operations: modulo, square, square root
    """
    
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def modulo(self, a: float, b: float) -> float:
        """
        Calculate the modulo (remainder) of a divided by b.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Remainder of a divided by b
            
        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        return a % b
    
    def square(self, a: float) -> float:
        """
        Calculate the square of a number.
        
        Args:
            a: Number to square
            
        Returns:
            Square of a
        """
        return a ** 2
    
    def square_root(self, a: float) -> float:
        """
        Calculate the square root of a number.
        
        Args:
            a: Number to find square root of
            
        Returns:
            Square root of a
            
        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
