"""Unit tests for the main program."""
import sys
from io import StringIO
import pytest

# Import the main module
import main


def test_main_prints_hello_2036(capsys):
    """Test that main() prints 'Hello 2036' to stdout."""
    main.main()
    captured = capsys.readouterr()
    assert captured.out == "Hello 2036\n"
    assert captured.err == ""


def test_main_output_exact_match():
    """Test that the output matches exactly 'Hello 2036'."""
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    try:
        main.main()
        output = sys.stdout.getvalue()
        assert output.strip() == "Hello 2036"
    finally:
        sys.stdout = old_stdout


def test_main_function_exists():
    """Test that main function exists and is callable."""
    assert hasattr(main, 'main')
    assert callable(main.main)
