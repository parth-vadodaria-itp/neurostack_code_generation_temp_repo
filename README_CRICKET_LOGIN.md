# Cricket Application - Login Page

## Story: KAN-87
**Develop a Login Page for the Cricket Application**

## Overview
This is a simple login page for the Cricket application built with Python Flask. The application validates user credentials against predefined values and provides appropriate feedback.

## Features Implemented

### ✅ Acceptance Criteria Met

1. **Login page displays Username and Password fields**
   - Clean, responsive form with labeled input fields
   - Professional cricket-themed design

2. **Login page contains a Login button**
   - Prominent submit button with hover effects
   - Accessible and user-friendly

3. **Empty username or password displays validation message**
   - Server-side validation checks for empty fields
   - Clear error message: "Please enter both username and password"

4. **Valid credentials display a welcome message**
   - Personalized welcome message with username
   - Dedicated welcome page after successful login

5. **Invalid credentials display error message**
   - Clear error message: "Invalid username or password"
   - Maintains security by not revealing which field is incorrect

6. **Password input is masked while typing**
   - Password field uses `type="password"` attribute
   - Characters are hidden for security

## Technology Stack

- **Language**: Python 3.11+
- **Framework**: Flask 3.1+
- **Template Engine**: Jinja2 (built-in with Flask)
- **Styling**: Custom CSS with gradient design
- **Configuration**: python-dotenv for environment variables

## Project Structure

```
cricket-login/
├── app.py                      # Main Flask application with routes
├── config.py                   # Configuration classes
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (not in git)
├── .env.example               # Example environment variables
├── .gitignore                 # Git ignore rules
├── templates/
│   ├── login.html             # Login form page
│   ├── welcome.html           # Success page
│   ├── 404.html               # Not found error page
│   └── 500.html               # Server error page
└── static/
    └── css/
        └── style.css          # Application styles
```

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Step 1: Clone or Navigate to Project
```bash
cd /path/to/cricket-login
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment
```bash
cp .env.example .env
# Edit .env if needed (default values work for development)
```

### Step 5: Run the Application
```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

### Accessing the Application
1. Open your web browser
2. Navigate to `http://localhost:5000`
3. You will be redirected to the login page

### Valid Credentials

The application has three predefined user accounts:

| Username      | Password    |
|---------------|-------------|
| admin         | cricket123  |
| user          | password    |
| cricket_fan   | ipl2024     |

### Testing Scenarios

#### Test 1: Successful Login
1. Enter username: `admin`
2. Enter password: `cricket123`
3. Click "Login"
4. **Expected**: Welcome page with success message

#### Test 2: Invalid Credentials
1. Enter username: `wronguser`
2. Enter password: `wrongpass`
3. Click "Login"
4. **Expected**: Error message "Invalid username or password"

#### Test 3: Empty Fields
1. Leave username empty
2. Enter any password
3. Click "Login"
4. **Expected**: Error message "Please enter both username and password"

#### Test 4: Password Masking
1. Click on password field
2. Type any characters
3. **Expected**: Characters appear as dots/asterisks

## API Endpoints

### `GET /`
- Redirects to login page

### `GET /login`
- Displays the login form

### `POST /login`
