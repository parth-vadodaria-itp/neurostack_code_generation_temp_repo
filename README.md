# Unit Converter Application

## Overview

A Python command-line application for converting values between commonly used units.

## Features

Supports the following conversion types:

- **Temperature**: Celsius ↔ Fahrenheit
- **Distance**: Kilometers ↔ Miles
- **Weight**: Kilograms ↔ Pounds
- **Length**: Centimeters ↔ Inches

## Requirements

- Python 3.11 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo.git
   cd neurostack_code_generation_temp_repo
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
python main.py
```

### Example Session

```
=== Unit Converter Application ===

Available conversion types:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Kilometers to Miles
4. Miles to Kilometers
5. Kilograms to Pounds
6. Pounds to Kilograms
7. Centimeters to Inches
8. Inches to Centimeters
9. Exit

Select conversion type (1-9): 1
Enter value to convert: 25
25.0 Celsius = 77.0 Fahrenheit
```

## Running Tests

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=converters --cov=validators --cov-report=html
```

## Project Structure

```
.
├── main.py                 # Application entry point
├── converters/
│   ├── __init__.py
│   ├── temperature.py      # Temperature conversion logic
│   ├── distance.py         # Distance conversion logic
│   ├── weight.py           # Weight conversion logic
│   └── length.py           # Length conversion logic
├── validators/
│   ├── __init__.py
│   └── input_validator.py  # Input validation logic
├── tests/
│   ├── __init__.py
│   ├── test_temperature.py
│   ├── test_distance.py
│   ├── test_weight.py
│   ├── test_length.py
│   └── test_validators.py
├── requirements.txt
└── README.md
```

## Acceptance Criteria

✅ User can select conversion type from menu
✅ Correct conversion is displayed for all supported unit types
✅ Invalid input is handled with clear error messages

## License

MIT License
