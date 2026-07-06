# Hello World Java Program

## Overview
A simple Java program that prints "Hello World" followed by a system-generated greeting message to the console.

## Story
- **Story ID**: KAN-79
- **Summary**: Develop Test Program
- **Description**: Develop a program with a single file containing a simple single function printing `Hello World` in Java.

## Requirements
- Java 17 or higher

## Project Structure
```
.
├── HelloWorld.java    # Main program file
├── README.md          # This file
├── .gitignore         # Git ignore rules
├── pom.xml            # Maven build configuration
└── CONTRIBUTING.md    # Development guide
```

## How to Run

### Option 1: Using javac (Java Compiler)
```bash
# Compile the program
javac HelloWorld.java

# Run the compiled program
java HelloWorld
```

### Option 2: Using Maven
```bash
# Compile
mvn compile

# Run
mvn exec:java -Dexec.mainClass="HelloWorld"
```

## Expected Output
```
Hello World
This is the system generated greeting. Don't reply!
```

## Acceptance Criteria
✅ Source code provided (HelloWorld.java)
✅ README documentation provided
✅ Ready for GitHub push

## Technical Details
- **Language**: Java 17
- **Build Tool**: Maven (optional)
- **Dependencies**: None (standalone program)

## Development
This is a minimal Java program with:
- One file: `HelloWorld.java`
- One function: `printHelloWorld()`
- Output: Two lines of text

## License
Proprietary - My Software Team (KAN Project)