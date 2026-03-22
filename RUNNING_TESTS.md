# Quick Guide: Running Individual Login Tests

## Setup (First Time Only)

1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```

## Running Individual Login Tests

### Method 1: Using the Menu Script (Easiest)
```bash
run_login_tests.bat
```
Then select the test you want to run from the menu.

### Method 2: Using Command Line

#### Run ALL login tests:
```bash
pytest tests/test_login.py -v -s
```

#### Run SPECIFIC individual tests:

**1. Test Successful Login:**
```bash
pytest tests/test_login.py::TestLogin::test_successful_login -v -s
```

**2. Test Invalid Username:**
```bash
pytest tests/test_login.py::TestLogin::test_login_invalid_username -v -s
```

**3. Test Invalid Password:**
```bash
pytest tests/test_login.py::TestLogin::test_login_invalid_password -v -s
```

**4. Test Empty Credentials:**
```bash
pytest tests/test_login.py::TestLogin::test_login_empty_credentials -v -s
```

**5. Test Empty Username:**
```bash
pytest tests/test_login.py::TestLogin::test_login_empty_username -v -s
```

**6. Test Empty Password:**
```bash
pytest tests/test_login.py::TestLogin::test_login_empty_password -v -s
```

**7. Test Logout:**
```bash
pytest tests/test_login.py::TestLogin::test_logout -v -s
```

**8. Test Remember Me:**
```bash
pytest tests/test_login.py::TestLogin::test_remember_me -v -s
```

### Method 3: Run by Test Markers

**Run only SMOKE tests:**
```bash
pytest tests/test_login.py -m smoke -v -s
```

**Run only REGRESSION tests:**
```bash
pytest tests/test_login.py -m regression -v -s
```

**Run only CRITICAL tests:**
```bash
pytest tests/test_login.py -m critical -v -s
```

## Generate Allure Report

After running tests, generate the report:
```bash
allure serve reports/allure-results
```

## Command Options Explained

- `-v` : Verbose output (shows test names)
- `-s` : Show print statements and logs
- `-m` : Run tests with specific marker
- `--alluredir` : Specify Allure results directory

## Test with Different Browsers

```bash
# Firefox
set BROWSER=firefox
pytest tests/test_login.py::TestLogin::test_successful_login -v -s

# WebKit (Safari)
set BROWSER=webkit
pytest tests/test_login.py::TestLogin::test_successful_login -v -s
```

## Test in Headless Mode

```bash
set HEADLESS=True
pytest tests/test_login.py::TestLogin::test_successful_login -v -s
```

## Demo Login Page

The framework includes a demo login page (`demo_login.html`) for testing.

**Valid Credentials:**
- Username: `testuser`
- Password: `testpass123`

**Invalid Credentials:**
- Any other username/password combination will fail

## Quick Test Example

To quickly test if everything works:
```bash
pytest tests/test_login.py::TestLogin::test_successful_login -v -s
```

This will:
1. Open the demo login page
2. Enter valid credentials
3. Click login
4. Verify successful login
5. Take a screenshot
6. Generate test report
