"""Main Calculator class combining basic and advanced operations."""

from calculator.basic_operations import BasicCalculator
from calculator.advanced_operations import AdvancedCalculator


class Calculator:
    """Unified calculator interface for all operations."""

    def __init__(self):
        """Initialize calculator with basic and advanced operation handlers."""
        self.basic = BasicCalculator()
        self.advanced = AdvancedCalculator()

    def add(self, a: float, b: float) -> float:
        """Add two numbers."""
        return self.basic.add(a, b)

    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a."""
        return self.basic.subtract(a, b)

    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers."""
        return self.basic.multiply(a, b)

    def divide(self, a: float, b: float) -> float:
        """Divide a by b."""
        return self.basic.divide(a, b)

    def modulo(self, a: float, b: float) -> float:
        """Calculate modulo of a divided by b."""
        return self.advanced.modulo(a, b)

    def square(self, a: float) -> float:
        """Calculate square of a number."""
        return self.advanced.square(a)

    def square_root(self, a: float) -> float:
        """Calculate square root of a number."""
        return self.advanced.square_root(a)
