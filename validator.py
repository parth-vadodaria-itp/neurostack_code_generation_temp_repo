"""Input validation module for student grade calculator.

This module provides validation functions for marks and subject counts.
"""

from typing import List, Tuple


class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass


class Validator:
    """Validates input data for the grade calculator."""

    MIN_MARKS = 0
    MAX_MARKS = 100
    MIN_SUBJECTS = 1
    MAX_SUBJECTS = 10

    @staticmethod
    def validate_marks(marks: float) -> Tuple[bool, str]:
        """Validate a single mark value.

        Args:
            marks: The mark value to validate

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(marks, (int, float)):
            return False, "Marks must be a number"

        if marks < Validator.MIN_MARKS or marks > Validator.MAX_MARKS:
            return False, f"Marks must be between {Validator.MIN_MARKS} and {Validator.MAX_MARKS}"

        return True, ""

    @staticmethod
    def validate_marks_list(marks_list: List[float]) -> Tuple[bool, str]:
        """Validate a list of marks.

        Args:
            marks_list: List of mark values to validate

        Returns:
            Tuple of (is_valid, error_message)

        Raises:
            ValidationError: If validation fails
        """
        if not marks_list:
            return False, "Marks list cannot be empty"

        if not isinstance(marks_list, list):
            return False, "Marks must be provided as a list"

        for idx, mark in enumerate(marks_list, 1):
            is_valid, error_msg = Validator.validate_marks(mark)
            if not is_valid:
                return False, f"Subject {idx}: {error_msg}"

        return True, ""

    @staticmethod
    def validate_subject_count(count: int) -> Tuple[bool, str]:
        """Validate the number of subjects.

        Args:
            count: Number of subjects

        Returns:
            Tuple of (is_valid, error_message)
        """
        if not isinstance(count, int):
            return False, "Subject count must be an integer"

        if count < Validator.MIN_SUBJECTS or count > Validator.MAX_SUBJECTS:
            return False, f"Number of subjects must be between {Validator.MIN_SUBJECTS} and {Validator.MAX_SUBJECTS}"

        return True, ""

    @staticmethod
    def parse_marks_input(input_str: str) -> float:
        """Parse marks input string to float.

        Args:
            input_str: String input from user

        Returns:
            Parsed float value

        Raises:
            ValidationError: If input cannot be parsed
        """
        try:
            marks = float(input_str.strip())
            return marks
        except ValueError:
            raise ValidationError(f"Invalid input: '{input_str}' is not a valid number")

    @staticmethod
    def parse_subject_count(input_str: str) -> int:
        """Parse subject count input string to integer.

        Args:
            input_str: String input from user

        Returns:
            Parsed integer value

        Raises:
            ValidationError: If input cannot be parsed
        """
        try:
            count = int(input_str.strip())
            return count
        except ValueError:
            raise ValidationError(f"Invalid input: '{input_str}' is not a valid integer")