#!/usr/bin/env python3
"""Command-line interface for the calculator application."""

import sys
from calculator import Calculator


def print_menu():
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("          PYTHON CALCULATOR")
    print("="*50)
    print("\nBasic Operations:")
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")
    print("\nAdvanced Operations:")
    print("  5. Modulo")
    print("  6. Square")
    print("  7. Square Root")
    print("\n  0. Exit")
    print("="*50)


def get_number(prompt: str) -> float:
    """Get a valid number from user input.
    
    Args:
        prompt: Input prompt message
        
    Returns:
        Valid float number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    """Main calculator application loop."""
    calc = Calculator()
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == "0":
                print("\nThank you for using Python Calculator. Goodbye!")
                sys.exit(0)
            
            if choice in ["1", "2", "3", "4", "5"]:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                
                if choice == "1":
                    result = calc.add(a, b)
                    print(f"\nResult: {a} + {b} = {result}")
                elif choice == "2":
                    result = calc.subtract(a, b)
                    print(f"\nResult: {a} - {b} = {result}")
                elif choice == "3":
                    result = calc.multiply(a, b)
                    print(f"\nResult: {a} × {b} = {result}")
                elif choice == "4":
                    result = calc.divide(a, b)
                    print(f"\nResult: {a} ÷ {b} = {result}")
                elif choice == "5":
                    result = calc.modulo(a, b)
                    print(f"\nResult: {a} % {b} = {result}")
            
            elif choice in ["6", "7"]:
                a = get_number("Enter number: ")
                
                if choice == "6":
                    result = calc.square(a)
                    print(f"\nResult: {a}² = {result}")
                elif choice == "7":
                    result = calc.square_root(a)
                    print(f"\nResult: √{a} = {result}")
            
            else:
                print("\nError: Invalid choice. Please select 0-7.")
                
        except ValueError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nInterrupted. Exiting...")
            sys.exit(0)
        except Exception as e:
            print(f"\nUnexpected error: {e}")


if __name__ == "__main__":
    main()
