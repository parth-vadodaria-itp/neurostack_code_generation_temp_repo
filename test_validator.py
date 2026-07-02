"""Unit tests for the validator module."""

import pytest
from validator import Validator, ValidationError


class TestValidateMarks:
    """Test cases for validate_marks method."""

    def test_valid_marks_integer(self):
        """Test validation with valid integer marks."""
        is_valid, error_msg = Validator.validate_marks(85)
        assert is_valid is True
        assert error_msg == ""

    def test_valid_marks_float(self):
        """Test validation with valid float marks."""
        is_valid, error_msg = Validator.validate_marks(85.5)
        assert is_valid is True
        assert error_msg == ""

    def test_valid_marks_boundary_min(self):
        """Test validation with minimum boundary value."""
        is_valid, error_msg = Validator.validate_marks(0)
        assert is_valid is True
        assert error_msg == ""

    def test_valid_marks_boundary_max(self):
        """Test validation with maximum boundary value."""
        is_valid, error_msg = Validator.validate_marks(100)
        assert is_valid is True
        assert error_msg == ""

    def test_invalid_marks_negative(self):
        """Test validation with negative marks."""
        is_valid, error_msg = Validator.validate_marks(-10)
        assert is_valid is False
        assert "must be between" in error_msg

    def test_invalid_marks_above_max(self):
        """Test validation with marks above maximum."""
        is_valid, error_msg = Validator.validate_marks(150)
        assert is_valid is False
        assert "must be between" in error_msg

    def test_invalid_marks_string(self):
        """Test validation with string input."""
        is_valid, error_msg = Validator.validate_marks("85")
        assert is_valid is False
        assert "must be a number" in error_msg

    def test_invalid_marks_none(self):
        """Test validation with None input."""
        is_valid, error_msg = Validator.validate_marks(None)
        assert is_valid is False
        assert "must be a number" in error_msg


class TestValidateMarksList:
    """Test cases for validate_marks_list method."""

    def test_valid_marks_list(self):
        """Test validation with valid marks list."""
        marks = [85, 90, 78, 92, 88]
        is_valid, error_msg = Validator.validate_marks_list(marks)
        assert is_valid is True
        assert error_msg == ""

    def test_valid_marks_list_with_floats(self):
        """Test validation with valid marks list containing floats."""
        marks = [85.5, 90.0, 78.75, 92.25, 88.5]
        is_valid, error_msg = Validator.validate_marks_list(marks)
        assert is_valid is True
        assert error_msg == ""

    def test_invalid_marks_list_empty(self):
        """Test validation with empty marks list."""
        is_valid, error_msg = Validator.validate_marks_list([])
        assert is_valid is False
        assert "cannot be empty" in error_msg

    def test_invalid_marks_list_not_list(self):
        """Test validation with non-list input."""
        is_valid, error_msg = Validator.validate_marks_list("not a list")
        assert is_valid is False
        assert "must be provided as a list" in error_msg

    def test_invalid_marks_list_contains_invalid(self):
        """Test validation with list containing invalid marks."""
        marks = [85, 90, 150, 92, 88]
        is_valid, error_msg = Validator.validate_marks_list(marks)
        assert is_valid is False
        assert "Subject 3"