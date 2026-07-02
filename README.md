# Calculator Application

A comprehensive Python calculator application supporting basic and advanced mathematical operations.

## Features

### Basic Operations
- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)

### Advanced Operations
- **Modulo**: Calculate the remainder of division
- **Square**: Calculate the square of a number
- **Square Root**: Calculate the square root of a number (with negative number protection)

## Requirements

- Python 3.11 or higher
- No external dependencies (uses Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo.git
cd neurostack_code_generation_temp_repo
```

2. No additional installation required (uses Python standard library only)

## Usage

### Command-Line Interface

Run the calculator application:

```bash
python main.py
```

Follow the on-screen menu to select operations:
- Enter numbers when prompted
- View results immediately
- Handle errors gracefully (division by zero, negative square roots, etc.)

### Programmatic Usage

Import and use the Calculator class in your own code:

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)          # 8
result = calc.subtract(10, 4)    # 6
result = calc.multiply(3, 7)     # 21
result = calc.divide(15, 3)      # 5.0

# Advanced operations
result = calc.modulo(17, 5)      # 2
result = calc.square(4)          # 16
result = calc.square_root(25)    # 5.0
```

## Running Tests

Execute the test suite:

```bash
python -m unittest test_calculator.py
```

Or run with verbose output:

```bash
python -m unittest test_calculator.py -v
```

## Docker Support

Build the Docker image:

```bash
docker build -t calculator-app .
```

Run the calculator in a container:

```bash
docker run -it calculator-app
```

## Project Structure

```
.
├── calculator.py          # Core calculator class with all operations
├── main.py               # Command-line interface
├── test_calculator.py    # Unit tests
├── requirements.txt      # Python dependencies (none required)
├── Dockerfile           # Container configuration
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Error Handling

The calculator includes robust error handling:
- **Division by zero**: Raises `ValueError` with descriptive message
- **Modulo by zero**: Raises `ValueError` with descriptive message
- **Negative square root**: Raises `ValueError` with descriptive message
- **Invalid input**: CLI prompts for valid numeric input

## Acceptance Criteria

✅ **AC1**: Calculator supports basic operations: addition, multiplication, subtraction, division  
✅ **AC2**: Calculator supports advanced operations: modulo, square, square root  
✅ **AC3**: Program is implemented in Python  
✅ **AC4**: Code is ready to be pushed to the specified GitHub repository

## License

This project is part of the KAN project (KAN-70).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## Support

For issues or questions, please create an issue in the GitHub repository.
