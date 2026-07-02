#!/usr/bin/env python3
"""Command-line interface for the Student Grade Calculator.

This module provides an interactive CLI for calculating student grades.
"""

import sys
from typing import List
from grade_calculator import GradeCalculator
from validator import Validator, ValidationError


def print_header():
    """Print application header."""
    print("\n" + "=" * 40)
    print("   Student Grade Calculator")
    print("=" * 40 + "\n")


def print_results(result: dict):
    """Print calculation results.

    Args:
        result: Dictionary containing calculation results
    """
    print("\n" + "=" * 40)
    print("   Results")
    print("=" * 40)
    print(f"Total Marks: {result['total']:.2f} / {result['max_possible']:.2f}")
    print(f"Average Marks: {result['average']:.2f}")
    print(f"Percentage: {result['percentage']:.2f}%")
    print(f"Grade: {result['grade']}")
    print("=" * 40 + "\n")


def get_subject_count() -> int:
    """Prompt user for number of subjects.

    Returns:
        Number of subjects

    Raises:
        ValidationError: If input is invalid
    """
    validator = Validator()

    while True:
        try:
            input_str = input(f"Enter number of subjects ({validator.MIN_SUBJECTS}-{validator.MAX_SUBJECTS}): ")
            count = validator.parse_subject_count(input_str)

            is_valid, error_msg = validator.validate_subject_count(count)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue

            return count

        except ValidationError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user.")
            sys.exit(0)


def get_marks(subject_count: int) -> List[float]:
    """Prompt user for marks for each subject.

    Args:
        subject_count: Number of subjects

    Returns:
        List of marks

    Raises:
        ValidationError: If input is invalid
    """
    validator = Validator()
    marks = []

    print()
    for i in range(1, subject_count + 1):
        while True:
            try:
                input_str = input(f"Enter marks for subject {i} ({validator.MIN_MARKS}-{validator.MAX_MARKS}): ")
                mark = validator.parse_marks_input(input_str)

                is_valid, error_msg = validator.validate_marks(mark)
                if not is_valid:
                    print(f"Error: {error_msg}")
                    continue

                marks.append(mark)
                break

            except ValidationError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\n\nOperation cancelled by user.")
                sys.exit(0)

    return marks


def main():
    """Main entry point for the CLI application."""
    try:
        print_header()

        calculator = GradeCalculator()

        subject_count = get_subject_count()
        marks = get_marks(subject_count)

        result = calculator.calculate(marks)
        print_results(result)

        return 0

    except ValidationError as e:
        print(f"\nValidation Error: {e}")
        return 1
    except ValueError as e:
        print(f"\nCalculation Error: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
        return 130
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())