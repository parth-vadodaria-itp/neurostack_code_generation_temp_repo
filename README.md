# Hello 2026 Python Program

A simple Python program that prints "Hello 2026" to the console.

## Requirements

- Python 3.11 or higher

## Usage

### Running Locally

```bash
python hello_2026.py
```

Or make it executable and run directly:

```bash
chmod +x hello_2026.py
./hello_2026.py
```

### Running with Docker

Build the Docker image:

```bash
docker build -t hello-2026 .
```

Run the container:

```bash
docker run hello-2026
```

## Output

```
Hello 2026
```

## Project Structure

```
.
├── hello_2026.py      # Main Python script
├── requirements.txt   # Python dependencies (empty for this simple script)
├── Dockerfile        # Docker configuration
├── .gitignore        # Git ignore patterns
└── README.md         # This file
```

## License

MIT
