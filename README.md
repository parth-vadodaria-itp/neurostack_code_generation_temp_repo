# Unit Converter Application

A Python application for converting values between commonly used units.

## Features

- **Temperature Conversion**: Celsius ↔ Fahrenheit
- **Distance Conversion**: Kilometers ↔ Miles
- **Weight Conversion**: Kilograms ↔ Pounds
- **Length Conversion**: Centimeters ↔ Inches

## Requirements

- Python 3.11 or higher
- tkinter (included with Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo.git
cd neurostack_code_generation_temp_repo
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies (for testing):
```bash
pip install -r requirements.txt
```

## Usage

### GUI Mode (Default)

Run the application with graphical interface:
```bash
python main.py
```

### CLI Mode

Run the application in command-line mode:
```bash
python main.py --cli
```

Follow the prompts to:
1. Select conversion type
2. Enter the value to convert
3. View the converted result

### Examples

**Temperature Conversion:**
```
Select conversion type: 1
Enter value in Celsius: 25
Result: 25.0°C = 77.0°F
```

**Distance Conversion:**
```
Select conversion type: 3
Enter value in Kilometers: 10
Result: 10.0 km = 6.21 miles
```

## Running Tests

```bash
pytest tests/ -v
```

With coverage report:
```bash
pytest tests/ -v --cov=converter --cov=cli --cov=gui
```

## Project Structure

```
.
├── converter/
│   ├── __init__.py
│   ├── temperature.py    # Temperature conversion logic
│   ├── distance.py       # Distance conversion logic
│   ├── weight.py         # Weight conversion logic
│   └── length.py         # Length conversion logic
├── cli.py                # Command-line interface
├── gui.py                # Graphical user interface
├── main.py               # Application entry point
├── tests/
│   ├── __init__.py
│   ├── test_temperature.py
│   ├── test_distance.py
│   ├── test_weight.py
│   └── test_length.py
├── requirements.txt
└── README.md
```

## License

MIT License