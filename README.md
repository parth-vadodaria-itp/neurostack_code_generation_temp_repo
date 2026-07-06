# Hello 2036 Python Program

A simple Python program that prints "Hello 2036" to the console.

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
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (none required for this simple program):
```bash
pip install -r requirements.txt
```

## Usage

Run the program:
```bash
python main.py
```

Or make it executable and run directly:
```bash
chmod +x main.py
./main.py
```

## Expected Output

```
Hello 2036
```

## Docker

You can also run this program using Docker:

```bash
# Build the image
docker build -t hello-2036 .

# Run the container
docker run hello-2036
```

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## License

MIT License
