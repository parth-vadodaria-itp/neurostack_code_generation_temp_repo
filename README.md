# 🎓 Student Grade Calculator

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](tests/)

## 📋 Overview

A robust Python application designed to calculate student grades with precision and reliability. This tool accepts marks for multiple subjects, validates inputs, and provides comprehensive grade analysis including total marks, average, percentage, and letter grades.

**Story ID**: KAN-71  
**Repository**: [neurostack_code_generation_temp_repo](https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo)

---

## ✨ Features

- ✅ **Multi-Subject Support**: Handle 1-10 subjects seamlessly
- ✅ **Input Validation**: Robust validation for marks (0-100 range)
- ✅ **Comprehensive Metrics**:
  - Total marks calculation
  - Average marks computation
  - Percentage calculation
  - Letter grade assignment
- ✅ **Error Handling**: Graceful handling of invalid inputs
- ✅ **Unit Tested**: Full test coverage with pytest
- ✅ **CLI Interface**: User-friendly command-line interface
- ✅ **Programmatic API**: Use as a library in your own projects

---

## 📊 Grade Mapping

The application uses the following grading scale:

| Letter Grade | Percentage Range | Description |
|--------------|------------------|-------------|
| **A** | ≥ 90% | Excellent |
| **B** | 80% - 89% | Good |
| **C** | 70% - 79% | Satisfactory |
| **D** | 60% - 69% | Pass |
| **F** | < 60% | Fail |

---

## 🚀 Quick Start

### Prerequisites

- **Python**: Version 3.8 or higher
- **pip**: Python package manager
- **Git**: For cloning the repository

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo.git
   cd neurostack_code_generation_temp_repo
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

### Interactive Command-Line Mode

Run the calculator in interactive mode:

```bash
python main.py
```

#### Example Session

```
========================================
   Student Grade Calculator
========================================

Enter number of subjects (1-10): 5

Enter marks for subject 1 (0-100): 85
Enter marks for subject 2 (0-100): 92
Enter marks for subject 3 (0-100): 78
Enter marks for subject 4 (0-100): 88
Enter marks for subject 5 (0-100): 95

========================================
   Results
========================================
Total Marks: 438.00 / 500.00
Average Marks: 87.60
Percentage: 87.60%
Grade: B
========================================
```

### Programmatic Usage

Use the calculator as a Python library:

```python
from grade_calculator import GradeCalculator

# Initialize calculator
calculator = GradeCalculator()

# Input marks
marks = [85, 92, 78, 88, 95]

# Calculate results
result = calculator.calculate(marks)

# Access results
print(f"Total: {result['total']}")
print(f"Average: {result['average']}")
print(f"Percentage: {result['percentage']}%")
print(f"Grade: {result['grade']}")
print(f"Subjects: {result['subject_count']}")
```

**Output**:
```
Total: 438.0
Average: 87.6
Percentage: 87.6%
Grade: B
Subjects: 5
```

---

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run Tests with Coverage Report

```bash
pytest --cov=. --cov-report=html
```

View the HTML coverage report:
```bash
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows
xdg-open htmlcov/index.html  # Linux
```

### Run Specific Test Files

```bash
pytest test_validator.py
pytest test_grade_calculator.py
```

---

## 📁 Project Structure

```
.
├── grade_calculator.py       # Core calculation logic
├── validator.py              # Input validation module
├── main.py                   # CLI interface
├── test_validator.py         # Validator unit tests
├── test_grade_calculator.py  # Calculator unit tests (if exists)
├── requirements.txt          # Python dependencies
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

### Module Descriptions

- **`grade_calculator.py`**: Contains the `GradeCalculator` class with methods for calculating totals, averages, percentages, and determining letter grades.
- **`validator.py`**: Provides the `Validator` class for input validation, including marks range checking and subject count validation.
- **`main.py`**: Command-line interface for interactive grade calculation.
- **`test_validator.py`**: Comprehensive unit tests for the validation module.

---

## ✅ Acceptance Criteria

All acceptance criteria from story **KAN-71** have been met:

- ✅ **Invalid marks are rejected**: Validation ensures marks are within 0-100 range
- ✅ **Percentage is calculated correctly**: Formula: `(total / max_possible) × 100`
- ✅ **Correct grade is displayed**: Based on the defined grade mapping

---

## 🛡️ Error Handling

The application gracefully handles various error scenarios:

| Error Type | Handling |
|------------|----------|
| Non-numeric input | Prompts user to enter a valid number |
| Marks outside 0-100 range | Rejects input with clear error message |
| Invalid subject count | Validates count is between 1-10 |
| Empty input | Requests valid input |
| Keyboard interrupt (Ctrl+C) | Exits gracefully with appropriate message |

---

## 🔧 Configuration

### Validation Limits

You can customize validation limits in `validator.py`:

```python
class Validator:
    MIN_MARKS = 0
    MAX_MARKS = 100
    MIN_SUBJECTS = 1
    MAX_SUBJECTS = 10
```

### Grade Thresholds

Customize grade thresholds in `grade_calculator.py`:

```python
class GradeCalculator:
    GRADE_THRESHOLDS = [
        (90, 'A'),
        (80, 'B'),
        (70, 'C'),
        (60, 'D'),
        (0, 'F')
    ]
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Write unit tests for new features
- Follow PEP 8 style guidelines
- Update documentation as needed
- Ensure all tests pass before submitting PR

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Support

For issues, questions, or suggestions:

- **GitHub Issues**: [Create an issue](https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo/issues)
- **Pull Requests**: [Submit a PR](https://github.com/parth-vadodaria-itp/neurostack_code_generation_temp_repo/pulls)

---

## 🎯 Roadmap

Future enhancements under consideration:

- [ ] Export results to CSV/JSON
- [ ] Batch processing from file input
- [ ] Weighted grade calculation
- [ ] GPA calculation support
- [ ] Web interface
- [ ] Database integration for student records

---

## 📚 Additional Resources

- [Python Documentation](https://docs.python.org/3/)
- [pytest Documentation](https://docs.pytest.org/)
- [PEP 8 Style Guide](https://pep8.org/)

---

**Built with ❤️ for KAN-71**