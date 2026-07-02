"""Core grade calculation module.

This module provides the main GradeCalculator class that computes
total marks, average, percentage, and letter grade.
"""

from typing import List, Dict
from validator import Validator, ValidationError


class GradeCalculator:
    """Calculates student grades based on marks."""

    GRADE_THRESHOLDS = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]

    def __init__(self):
        """Initialize the grade calculator."""
        self.validator = Validator()

    def calculate_total(self, marks: List[float]) -> float:
        """Calculate total marks.

        Args:
            marks: List of marks for each subject

        Returns:
            Total of all marks
        """
        return sum(marks)

    def calculate_average(self, marks: List[float]) -> float:
        """Calculate average marks.

        Args:
            marks: List of marks for each subject

        Returns:
            Average of all marks

        Raises:
            ValueError: If marks list is empty
        """
        if not marks:
            raise ValueError("Cannot calculate average of empty marks list")

        return self.calculate_total(marks) / len(marks)

    def calculate_percentage(self, marks: List[float], max_marks_per_subject: float = 100.0) -> float:
        """Calculate percentage.

        Args:
            marks: List of marks for each subject
            max_marks_per_subject: Maximum marks possible per subject (default: 100)

        Returns:
            Percentage score

        Raises:
            ValueError: If marks list is empty or max_marks is invalid
        """
        if not marks:
            raise ValueError("Cannot calculate percentage of empty marks list")

        if max_marks_per_subject <= 0:
            raise ValueError("Maximum marks must be greater than zero")

        total_marks = self.calculate_total(marks)
        max_possible = len(marks) * max_marks_per_subject
        percentage = (total_marks / max_possible) * 100

        return round(percentage, 2)

    def determine_grade(self, percentage: float) -> str:
        """Determine letter grade based on percentage.

        Grade mapping:
        - A: >= 90%
        - B: 80% - 89%
        - C: 70% - 79%
        - D: 60% - 69%
        - F: < 60%

        Args:
            percentage: Percentage score

        Returns:
            Letter grade (A, B, C, D, or F)

        Raises:
            ValueError: If percentage is negative or greater than 100
        """
        if percentage < 0 or percentage > 100:
            raise ValueError(f"Percentage must be between 0 and 100, got {percentage}")

        for threshold, grade in self.GRADE_THRESHOLDS:
            if percentage >= threshold:
                return grade

        return 'F'

    def calculate(self, marks: List[float], max_marks_per_subject: float = 100.0) -> Dict[str, any]:
        """Calculate all grade metrics.

        Args:
            marks: List of marks for each subject
            max_marks_per_subject: Maximum marks possible per subject (default: 100)

        Returns:
            Dictionary containing:
                - total: Total marks
                - average: Average marks
                - percentage: Percentage score
                - grade: Letter grade
                - max_possible: Maximum possible marks
                - subject_count: Number of subjects

        Raises:
            ValidationError: If marks validation fails
            ValueError: If calculation fails
        """
        is_valid, error_msg = self.validator.validate_marks_list(marks)
        if not is_valid:
            raise ValidationError(error_msg)

        total = self.calculate_total(marks)
        average = self.calculate_average(marks)
        percentage = self.calculate_percentage(marks, max_marks_per_subject)
        grade = self.determine_grade(percentage)
        max_possible = len(marks) * max_marks_per_subject

        return {
            'total': round(total, 2),
            'average': round(average, 2),
            'percentage': percentage,
            'grade': grade,
            'max_possible': max_possible,
            'subject_count': len(marks)
        }