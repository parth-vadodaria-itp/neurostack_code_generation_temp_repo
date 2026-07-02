"""
Command-line interface for the calculator application.
"""
from calculator import Calculator


def print_menu():
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("CALCULATOR APPLICATION")
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
    """
    Get a number from user input with validation.
    
    Args:
        prompt: Prompt message to display
        
    Returns:
        Valid float number
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main function to run the calculator CLI."""
    calc = Calculator()
    
    print("\nWelcome to the Calculator Application!")
    
    while True:
        print_menu()
        
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == "0":
                print("\nThank you for using the Calculator. Goodbye!")
                break
            
            if choice == "1":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            
            elif choice == "2":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            
            elif choice == "3":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"\nResult: {a} × {b} = {result}")
            
            elif choice == "4":
                a = get_number("Enter numerator: ")
                b = get_number("Enter denominator: ")
                try:
                    result = calc.divide(a, b)
                    print(f"\nResult: {a} ÷ {b} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            elif choice == "5":
                a = get_number("Enter dividend: ")
                b = get_number("Enter divisor: ")
                try:
                    result = calc.modulo(a, b)
                    print(f"\nResult: {a} mod {b} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            elif choice == "6":
                a = get_number("Enter number to square: ")
                result = calc.square(a)
                print(f"\nResult: {a}² = {result}")
            
            elif choice == "7":
                a = get_number("Enter number for square root: ")
                try:
                    result = calc.square_root(a)
                    print(f"\nResult: √{a} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
            
            else:
                print("\nInvalid choice. Please select a number between 0 and 7.")
        
        except KeyboardInterrupt:
            print("\n\nOperation cancelled. Returning to menu...")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
