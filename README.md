# Unit Converter Application

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A Python command-line application for converting values between commonly used units.

## Features

### Supported Conversions

- **Temperature**: Celsius ↔ Fahrenheit
- **Distance**: Kilometers ↔ Miles
- **Weight**: Kilograms ↔ Pounds
- **Length**: Centimeters ↔ Inches

### Key Capabilities

✅ Interactive menu-driven interface  
✅ Input validation and error handling  
✅ Precise conversion formulas  
✅ Bidirectional conversions  
✅ Clean, formatted output  
✅ Comprehensive unit tests  

## Requirements

- Python 3.11 or higher
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo.git
cd neurostack_code_generation_temp_repo
```

2. Verify Python version:
```bash
python --version
```

## Usage

### Running the Application

```bash
python unit_converter.py
```

### Example Session

```
Welcome to the Unit Converter Application!

==================================================
Unit Converter Application
==================================================

Select a conversion type:

1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Kilometers to Miles
4. Miles to Kilometers
5. Kilograms to Pounds
6. Pounds to Kilograms
7. Centimeters to Inches
8. Inches to Centimeters
0. Exit

Enter your choice (0-8): 1

Celsius to Fahrenheit
----------------------------------------
Enter value in °C: 25

✓ Result: 25.00 °C = 77.00 °F

Press Enter to continue...
```

## Testing

### Run Unit Tests

```bash
python -m unittest test_unit_converter.py
```

### Run Tests with Verbose Output

```bash
python -m unittest test_unit_converter.py -v
```

### Test Coverage

The test suite includes:
- Individual conversion function tests
- Round-trip conversion validation
- Edge case testing (zero values, negative values)
- Floating-point precision validation

## Project Structure

```
neurostack_code_generation_temp_repo/
├── unit_converter.py          # Main application
├── test_unit_converter.py     # Unit tests
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
└── LICENSE                    # License file
```

## Conversion Formulas

### Temperature
- **Celsius to Fahrenheit**: `F = (C × 9/5) + 32`
- **Fahrenheit to Celsius**: `C = (F - 32) × 5/9`

### Distance
- **Kilometers to Miles**: `mi = km × 0.621371`
- **Miles to Kilometers**: `km = mi × 1.60934`

### Weight
- **Kilograms to Pounds**: `lb = kg × 2.20462`
- **Pounds to Kilograms**: `kg = lb × 0.453592`

### Length
- **Centimeters to Inches**: `in = cm × 0.393701`
- **Inches to Centimeters**: `cm = in × 2.54`

## Error Handling

The application handles:
- Invalid menu selections
- Non-numeric input values
- Keyboard interrupts (Ctrl+C)
- Unexpected runtime errors

## Development

### Code Style

The code follows:
- PEP 8 style guidelines
- Type hints for function signatures
- Comprehensive docstrings
- Clean architecture principles

### Adding New Conversions

1. Add conversion methods to `UnitConverter` class
2. Update `CONVERSION_OPTIONS` dictionary in `ConverterUI`
3. Add corresponding unit tests
4. Update README documentation

## Acceptance Criteria

✅ **User selects conversion type**: Interactive menu with 8 conversion options  
✅ **Correct conversion is displayed**: Accurate formulas with 2 decimal precision  
✅ **Invalid input is handled**: Comprehensive validation and error messages  

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Story Reference

**Jira Story**: KAN-72  
**Summary**: Develop a Unit Converter Application  
**Status**: In Progress  

## Contact

For questions or issues, please open a GitHub issue in the repository.
