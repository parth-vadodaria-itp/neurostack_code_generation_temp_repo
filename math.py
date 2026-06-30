"""Math Utility Module

Provides basic mathematical operations and utility functions.
"""

import math
from typing import Union, List


class MathOperations:
    """A class containing various mathematical operations and utilities."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
        """
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b.
        
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

    @staticmethod
    def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Raise base to the power of exponent.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent

    @staticmethod
    def square_root(n: Union[int, float]) -> float:
        """Calculate the square root of n.
        
        Args:
            n: Number to find square root of
            
        Returns:
            Square root of n
            
        Raises:
            ValueError: If n is negative
        """
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(n)

    @staticmethod
    def factorial(n: int) -> int:
        """Calculate the factorial of n.
        
        Args:
            n: Non-negative integer
            
        Returns:
            Factorial of n
            
        Raises:
            ValueError: If n is negative or not an integer
        """
        if not isinstance(n, int):
            raise ValueError("Factorial requires an integer")
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)

    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is prime.
        
        Args:
            n: Number to check
            
        Returns:
            True if n is prime, False otherwise
        """
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """Calculate the greatest common divisor of a and b.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            Greatest common divisor of a and b
        """
        return math.gcd(a, b)

    @staticmethod
    def lcm(a: int, b: int) -> int:
        """Calculate the least common multiple of a and b.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            Least common multiple of a and b
        """
        return abs(a * b) // math.gcd(a, b) if a and b else 0

    @staticmethod
    def average(numbers: List[Union[int, float]]) -> float:
        """Calculate the average of a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Average of the numbers
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate average of empty list")
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Calculate the median of a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Median of the numbers
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate median of empty list")
        sorted_numbers = sorted(numbers)
        n = len(sorted_numbers)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
        return sorted_numbers[mid]

    @staticmethod
    def mode(numbers: List[Union[int, float]]) -> Union[int, float]:
        """Find the mode (most frequent value) in a list of numbers.
        
        Args:
            numbers: List of numbers
            
        Returns:
            Most frequent number
            
        Raises:
            ValueError: If the list is empty
        """
        if not numbers:
            raise ValueError("Cannot calculate mode of empty list")
        from collections import Counter
        count = Counter(numbers)
        return count.most_common(1)[0][0]


def main():
    """Example usage of MathOperations class."""
    math_ops = MathOperations()
    
    print("Basic Operations:")
    print(f"10 + 5 = {math_ops.add(10, 5)}")
    print(f"10 - 5 = {math_ops.subtract(10, 5)}")
    print(f"10 * 5 = {math_ops.multiply(10, 5)}")
    print(f"10 / 5 = {math_ops.divide(10, 5)}")
    print(f"2 ^ 8 = {math_ops.power(2, 8)}")
    print(f"√16 = {math_ops.square_root(16)}")
    
    print("\nAdvanced Operations:")
    print(f"5! = {math_ops.factorial(5)}")
    print(f"Is 17 prime? {math_ops.is_prime(17)}")
    print(f"GCD(48, 18) = {math_ops.gcd(48, 18)}")
    print(f"LCM(12, 15) = {math_ops.lcm(12, 15)}")
    
    print("\nStatistical Operations:")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Average of {numbers} = {math_ops.average(numbers)}")
    print(f"Median of {numbers} = {math_ops.median(numbers)}")
    numbers_with_mode = [1, 2, 2, 3, 3, 3, 4, 5]
    print(f"Mode of {numbers_with_mode} = {math_ops.mode(numbers_with_mode)}")


if __name__ == "__main__":
    main()
