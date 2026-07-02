# Student Grade Calculator

## Overview

A Python application that calculates a student's total marks, percentage, and grade based on marks entered for multiple subjects.

## Features

- Accept marks for multiple subjects (1-10 subjects)
- Validate input marks (0-100 range)
- Calculate:
  - Total marks
  - Average marks
  - Percentage
  - Letter grade
- Comprehensive error handling for invalid inputs
- Unit tested with pytest

## Grade Mapping

| Grade | Percentage Range |
|-------|------------------|
| A     | ≥ 90%           |
| B     | 80% - 89%       |
| C     | 70% - 79%       |
| D     | 60% - 69%       |
| F     | < 60%           |

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo.git
cd neurostack_code_generation_temp_repo
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive Mode

Run the calculator in interactive mode:

```bash
python main.py
```

Follow the prompts:
1. Enter the number of subjects (1-10)
2. Enter marks for each subject (0-100)
3. View the calculated results

### Example Session

```
=== Student Grade Calculator ===

Enter number of subjects (1-10): 5

Enter marks for subject 1 (0-100): 85
Enter marks for subject 2 (0-100): 92
Enter marks for subject 3 (0-100): 78
Enter marks for subject 4 (0-100): 88
Enter marks for subject 5 (0-100): 95

=== Results ===
Total Marks: 438.00 / 500.00
Average Marks: 87.60
Percentage: 87.60%
Grade: B
```

### Programmatic Usage

```python
from grade_calculator import GradeCalculator

calculator = GradeCalculator()
marks = [85, 92, 78, 88, 95]

result = calculator.calculate(marks)
print(f"Total: {result['total']}")
print(f"Percentage: {result['percentage']}%")
print(f"Grade: {result['grade']}")
```

## Running Tests

Run the test suite:

```bash
pytest
```

Run tests with coverage report:

```bash
pytest --cov=. --cov-report=html
```

## Project Structure

```
.
├── grade_calculator.py    # Core calculation logic
├── validator.py           # Input validation
├── main.py               # CLI interface
├── test_grade_calculator.py  # Unit tests for calculator
├── test_validator.py     # Unit tests for validator
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Acceptance Criteria

✅ Invalid marks are rejected (validation for 0-100 range)
✅ Percentage is calculated correctly (total/max_possible * 100)
✅ Correct grade is displayed (based on grade mapping)

## Error Handling

The application handles:
- Non-numeric input
- Marks outside 0-100 range
- Invalid number of subjects
- Empty input

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Story Reference

**Story ID**: KAN-71  
**Summary**: Develop a Student Grade Calculator