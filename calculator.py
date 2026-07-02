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
        Calculate the square of a number using custom loop-based multiplication.
        
        This implementation uses iterative addition to multiply the number by itself,
        avoiding the use of the ** operator.
        
        Args:
            a: Number to square
            
        Returns:
            Square of a
        """
        # Handle zero case
        if a == 0:
            return 0
        
        # Work with absolute value for calculation
        abs_a = abs(a)
        
        # Convert to integer representation for loop-based multiplication
        # For floating point numbers, we'll use a scaled approach
        is_negative = a < 0
        
        # Perform multiplication using repeated addition
        # result = a * a, implemented as adding 'a' to itself 'a' times
        result = 0.0
        
        # For integer part multiplication
        int_part = int(abs_a)
        frac_part = abs_a - int_part
        
        # Square the integer part using loop
        for i in range(int_part):
            for j in range(int_part):
                result += 1
        
        # Add the cross terms: 2 * int_part * frac_part
        for i in range(int_part):
            result += 2 * frac_part
        
        # Add the fractional part squared: frac_part * frac_part
        result += frac_part * frac_part
        
        # Square of any real number (positive or negative) is always positive
        return result
    
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
