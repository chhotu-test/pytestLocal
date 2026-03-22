# UI Testing Framework with Python, Playwright, Pytest & Allure

A scalable and comprehensive UI testing framework built with Python, Playwright, Pytest, and Allure reporting for automated web application testing.

## Features

- **Page Object Model (POM)** design pattern for maintainable test code
- **Playwright** for cross-browser automation (Chromium, Firefox, WebKit)
- **Pytest** as the test runner with powerful fixtures and plugins
- **Allure Reports** for beautiful and detailed test reporting
- **Screenshot on failure** automatically captures screenshots when tests fail
- **Configurable** via environment variables and config files
- **Parallel execution** support for faster test runs
- **Comprehensive logging** with file and console output
- **Reusable utilities** for common test operations

## Project Structure

```
PyTest/
├── config/
│   └── config.py              # Configuration management
├── pages/
│   ├── base_page.py           # Base page with common methods
│   └── login_page.py          # Login page object model
├── tests/
│   └── test_login.py          # Login test cases
├── utils/
│   ├── logger.py              # Logging utility
│   ├── screenshot_helper.py   # Screenshot utility
│   └── test_data_helper.py    # Test data generation
├── reports/
│   ├── allure-results/        # Allure test results
│   └── allure-report/         # Generated Allure reports
├── screenshots/               # Test screenshots
├── logs/                      # Test execution logs
├── conftest.py               # Pytest fixtures and hooks
├── pytest.ini                # Pytest configuration
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment variables
└── README.md                # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Java 8+ (for Allure report generation)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd PyTest
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

6. **Install Allure (if not already installed):**
   - Windows (using Scoop):
     ```bash
     scoop install allure
     ```
   - Mac (using Homebrew):
     ```bash
     brew install allure
     ```
   - Linux:
     ```bash
     sudo apt-add-repository ppa:qameta/allure
     sudo apt-get update
     sudo apt-get install allure
     ```

7. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your configuration values.

## Configuration

Edit the `.env` file to customize your test execution:

```env
BASE_URL=https://example.com
BROWSER=chromium                    # chromium, firefox, or webkit
HEADLESS=False                      # True for headless mode
SLOW_MO=0                          # Slow down operations (milliseconds)
TIMEOUT=30000                      # Default timeout (milliseconds)
SCREENSHOT_ON_FAILURE=True         # Capture screenshot on test failure
VIDEO_ON_FAILURE=False             # Record video on test failure
VIEWPORT_WIDTH=1920
VIEWPORT_HEIGHT=1080
PARALLEL_WORKERS=1                 # Number of parallel workers

VALID_USERNAME=testuser
VALID_PASSWORD=testpass123
INVALID_USERNAME=invaliduser
INVALID_PASSWORD=wrongpass
```

## Running Tests

### Run all tests:
```bash
pytest
```

### Run tests with specific markers:
```bash
pytest -m smoke                    # Run smoke tests only
pytest -m login                    # Run login tests only
pytest -m "smoke and critical"     # Run smoke AND critical tests
pytest -m "smoke or regression"    # Run smoke OR regression tests
```

### Run specific test file:
```bash
pytest tests/test_login.py
```

### Run specific test:
```bash
pytest tests/test_login.py::TestLogin::test_successful_login
```

### Run tests in parallel:
```bash
pytest -n 4                        # Run with 4 workers
```

### Run tests with verbose output:
```bash
pytest -v -s
```

### Run tests in different browsers:
```bash
BROWSER=firefox pytest
BROWSER=webkit pytest
```

### Run tests in headless mode:
```bash
HEADLESS=True pytest
```

## Generating Allure Reports

### Generate and open Allure report:
```bash
allure serve reports/allure-results
```

### Generate Allure report to a directory:
```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

### Open existing Allure report:
```bash
allure open reports/allure-report
```

## Test Markers

The framework includes the following test markers:

- `@pytest.mark.smoke` - Smoke tests (critical functionality)
- `@pytest.mark.regression` - Regression tests (full test suite)
- `@pytest.mark.login` - Login functionality tests
- `@pytest.mark.critical` - Critical test cases

## Writing New Tests

### 1. Create a new page object (if needed):

```python
from pages.base_page import BasePage
import allure

class MyPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.my_element = "#my-element"
    
    @allure.step("Perform action")
    def perform_action(self):
        self.click(self.my_element)
```

### 2. Create a new test file:

```python
import pytest
import allure
from pages.my_page import MyPage

@allure.feature("My Feature")
@allure.suite("My Test Suite")
class TestMyFeature:
    
    @allure.title("Test my functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_my_functionality(self, page, base_url):
        my_page = MyPage(page)
        
        with allure.step("Open page"):
            my_page.navigate(base_url)
        
        with allure.step("Perform action"):
            my_page.perform_action()
        
        with allure.step("Verify result"):
            assert my_page.is_visible(".result")
```

## Utilities

### Logger:
```python
from utils.logger import Logger

logger = Logger.setup_logger("my_test")
logger.info("Test started")
logger.error("Test failed")
```

### Screenshot Helper:
```python
from utils.screenshot_helper import ScreenshotHelper

ScreenshotHelper.capture_screenshot(page, "my_screenshot")
ScreenshotHelper.capture_element_screenshot(page, "#element", "element_screenshot")
```

### Test Data Helper:
```python
from utils.test_data_helper import TestDataHelper

email = TestDataHelper.generate_random_email()
password = TestDataHelper.generate_random_password()
username = TestDataHelper.generate_random_username()
```

## CI/CD Integration

### Example GitHub Actions workflow:

```yaml
name: UI Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install --with-deps
      - name: Run tests
        run: pytest --alluredir=reports/allure-results
      - name: Generate Allure report
        if: always()
        run: allure generate reports/allure-results -o reports/allure-report
      - name: Upload Allure report
        if: always()
        uses: actions/upload-artifact@v2
        with:
          name: allure-report
          path: reports/allure-report
```

## Best Practices

1. **Use Page Object Model** - Keep page elements and actions in page classes
2. **Add Allure steps** - Use `@allure.step()` decorator for better reporting
3. **Use fixtures** - Leverage pytest fixtures for setup and teardown
4. **Add markers** - Tag tests with appropriate markers for selective execution
5. **Take screenshots** - Capture screenshots for debugging failed tests
6. **Use meaningful names** - Name tests and methods descriptively
7. **Keep tests independent** - Each test should be able to run independently
8. **Use configuration** - Externalize configuration via environment variables

## Troubleshooting

### Playwright browsers not installed:
```bash
playwright install
```

### Allure command not found:
Install Allure command-line tool (see Installation section)

### Tests failing due to timeout:
Increase timeout in `.env` file or use `page.set_default_timeout(60000)`

### Screenshots not captured:
Ensure `SCREENSHOT_ON_FAILURE=True` in `.env` file

## Contributing

1. Create a new branch for your feature
2. Write tests following the existing patterns
3. Ensure all tests pass
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please create an issue in the project repository.
