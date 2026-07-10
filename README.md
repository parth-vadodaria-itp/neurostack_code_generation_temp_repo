# Unit Converter Application

A Python command-line application for converting values between commonly used units.

## Features

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

2. (Optional) Create a virtual environment:
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
python converter.py
```

Follow the on-screen menu to:
1. Select a conversion type
2. Enter the value to convert
3. View the converted result

## Running Tests

```bash
pytest tests/
```

## Docker

Build and run using Docker:
```bash
docker build -t unit-converter .
docker run -it unit-converter
```

## Project Structure

```
unit_converter/
├── converter.py       # Main CLI application
├── conversions.py     # Conversion logic
├── validators.py      # Input validation
├── tests/             # Unit tests
├── requirements.txt   # Dependencies
├── Dockerfile         # Container configuration
└── README.md          # Documentation
```

## License

MIT
