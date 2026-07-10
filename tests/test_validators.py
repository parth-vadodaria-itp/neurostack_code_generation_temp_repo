"""
Unit tests for input validation functions.
"""

import pytest
from validators import validate_numeric_input, validate_menu_choice


class TestValidateNumericInput:
    """Test numeric input validation."""
    
    def test_valid_integer(self):
        """Test valid integer input."""
        assert validate_numeric_input("42") == 42.0
    
    def test_valid_float(self):
        """Test valid float input."""
        assert validate_numeric_input("3.14") == 3.14
    
    def test_valid_negative(self):
        """Test valid negative number."""
        assert validate_numeric_input("-10.5") == -10.5
    
    def test_valid_zero(self):
        """Test zero input."""
        assert validate_numeric_input("0") == 0.0
    
    def test_valid_scientific_notation(self):
        """Test scientific notation input."""
        assert validate_numeric_input("1e3") == 1000.0
    
    def test_invalid_empty_string(self):
        """Test empty string raises ValueError."""
        with pytest.raises(ValueError, match="Input cannot be empty"):
            validate_numeric_input("")
    
    def test_invalid_text(self):
        """Test text input raises ValueError."""
        with pytest.raises(ValueError, match="not a valid number"):
            validate_numeric_input("abc")
    
    def test_invalid_mixed(self):
        """Test mixed text/number input raises ValueError."""
        with pytest.raises(ValueError, match="not a valid number"):
            validate_numeric_input("12abc")


class TestValidateMenuChoice:
    """Test menu choice validation."""
    
    def test_valid_choice_minimum(self):
        """Test minimum valid choice."""
        assert validate_menu_choice("1", 1, 9) == 1
    
    def test_valid_choice_maximum(self):
        """Test maximum valid choice."""
        assert validate_menu_choice("9", 1, 9) == 9
    
    def test_valid_choice_middle(self):
        """Test middle range choice."""
        assert validate_menu_choice("5", 1, 9) == 5
    
    def test_invalid_empty_string(self):
        """Test empty string raises ValueError."""
        with pytest.raises(ValueError, match="Choice cannot be empty"):
            validate_menu_choice("", 1, 9)
    
    def test_invalid_text(self):
        """Test text input raises ValueError."""
        with pytest.raises(ValueError, match="not a valid menu option"):
            validate_menu_choice("abc", 1, 9)
    
    def test_invalid_below_minimum(self):
        """Test choice below minimum raises ValueError."""
        with pytest.raises(ValueError, match="Choice must be between"):
            validate_menu_choice("0", 1, 9)
    
    def test_invalid_above_maximum(self):
        """Test choice above maximum raises ValueError."""
        with pytest.raises(ValueError, match="Choice must be between"):
            validate_menu_choice("10", 1, 9)
    
    def test_invalid_negative(self):
        """Test negative choice raises ValueError."""
        with pytest.raises(ValueError, match="Choice must be between"):
            validate_menu_choice("-1", 1, 9)
    
    def test_custom_range(self):
        """Test custom min/max range."""
        assert validate_menu_choice("5", 3, 7) == 5
        
        with pytest.raises(ValueError):
            validate_menu_choice("2", 3, 7)
        
        with pytest.raises(ValueError):
            validate_menu_choice("8", 3, 7)
