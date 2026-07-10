"""Unit tests for the validator module."""

import pytest
import math
from unit_converter.validator import InputValidator


class TestInputValidator:
    """Test cases for InputValidator class."""

    @pytest.fixture
    def validator(self):
        """Create an InputValidator instance for testing."""
        return InputValidator()

    def test_is_valid_number_with_valid_inputs(self, validator):
        """Test is_valid_number with valid numeric inputs."""
        assert validator.is_valid_number(0) is True
        assert validator.is_valid_number(10) is True
        assert validator.is_valid_number(-10) is True
        assert validator.is_valid_number(3.14) is True
        assert validator.is_valid_number(-3.14) is True
        assert validator.is_valid_number(1e10) is True

    def test_is_valid_number_with_invalid_inputs(self, validator):
        """Test is_valid_number with invalid inputs."""
        assert validator.is_valid_number(float('nan')) is False
        assert validator.is_valid_number(float('inf')) is False
        assert validator.is_valid_number(float('-inf')) is False
        assert validator.is_valid_number("string") is False
        assert validator.is_valid_number(None) is False
        assert validator.is_valid_number([]) is False

    def test_is_positive_number(self, validator):
        """Test is_positive_number validation."""
        assert validator.is_positive_number(1) is True
        assert validator.is_positive_number(0.1) is True
        assert validator.is_positive_number(1000) is True

        assert validator.is_positive_number(0) is False
        assert validator.is_positive_number(-1) is False
        assert validator.is_positive_number(-0.1) is False

    def test_is_in_range(self, validator):
        """Test is_in_range validation."""
        assert validator.is_in_range(5, 0, 10) is True
        assert validator.is_in_range(0, 0, 10) is True
        assert validator.is_in_range(10, 0, 10) is True
        assert validator.is_in_range(5.5, 0, 10) is True

        assert validator.is_in_range(-1, 0, 10) is False
        assert validator.is_in_range(11, 0, 10) is False
        assert validator.is_in_range(float('nan'), 0, 10) is False
