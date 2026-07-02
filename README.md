# Unit Converter Application

A Python application for converting values between commonly used units.

## Features

Supports the following conversions:

- **Temperature**: Celsius ↔ Fahrenheit
- **Distance**: Kilometers ↔ Miles
- **Weight**: Kilograms ↔ Pounds
- **Length**: Centimeters ↔ Inches

## Requirements

- Python 3.11 or higher

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

3. Install dependencies (for testing):
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

Follow the on-screen prompts to:
1. Select a conversion type
2. Enter the value to convert
3. View the converted result

### Example

```
=== Unit Converter Application ===

Available conversions:
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
├── main.py                    # Application entry point
├── converters/
│   ├── __init__.py
│   ├── temperature.py         # Temperature conversions
│   ├── distance.py            # Distance conversions
│   ├── weight.py              # Weight conversions
│   └── length.py              # Length conversions
├── validators/
│   ├── __init__.py
│   └── input_validator.py     # Input validation logic
├── ui/
│   ├── __init__.py
│   └── menu.py                # User interface
├── tests/
│   ├── __init__.py
│   ├── test_temperature.py
│   ├── test_distance.py
│   ├── test_weight.py
│   ├── test_length.py
│   └── test_validators.py
├── requirements.txt
├── .gitignore
└── README.md
```

## License

MIT