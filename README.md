# Unit Converter Application

## Overview

A Python application for converting values between commonly used units.

## Supported Conversions

- **Temperature**: Celsius ↔ Fahrenheit
- **Distance**: Kilometers ↔ Miles
- **Weight**: Kilograms ↔ Pounds
- **Length**: Centimeters ↔ Inches

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

```bash
python cli.py
```

Follow the interactive prompts to:
1. Select a conversion type
2. Enter the value to convert
3. View the converted result

### Graphical User Interface (Optional)

```bash
python gui.py
```

A simple GUI window will open where you can:
- Select conversion type from dropdown
- Enter value in the input field
- Click "Convert" to see the result

### Programmatic Usage

```python
from converters.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converters.distance import kilometers_to_miles, miles_to_kilometers
from converters.weight import kilograms_to_pounds, pounds_to_kilograms
from converters.length import centimeters_to_inches, inches_to_centimeters

# Temperature conversion
temp_f = celsius_to_fahrenheit(25.0)
print(f"25°C = {temp_f}°F")

# Distance conversion
dist_miles = kilometers_to_miles(10.0)
print(f"10 km = {dist_miles} miles")
```

## Running Tests

```bash
pytest tests/ -v
```

With coverage:

```bash
pytest tests/ --cov=converters --cov-report=html
```

## Project Structure

```
unit-converter/
├── converters/
│   ├── __init__.py
│   ├── temperature.py
│   ├── distance.py
│   ├── weight.py
│   └── length.py
├── tests/
│   ├── __init__.py
│   ├── test_temperature.py
│   ├── test_distance.py
│   ├── test_weight.py
│   └── test_length.py
├── cli.py
├── gui.py
├── requirements.txt
└── README.md
```

## Error Handling

The application validates all inputs and provides clear error messages for:
- Non-numeric input values
- Invalid conversion type selections
- Out-of-range values

## License

MIT