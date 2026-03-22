# Quick Start Guide

## ✅ Framework Setup Complete!

Your UI Testing Framework is now fully functional with:
- ✅ Python 3.13.2
- ✅ Playwright 1.58.0
- ✅ Pytest 7.4.3
- ✅ Allure Reporting 2.13.2
- ✅ All 8 login tests passing

## Running Tests

### Run All Tests
```bash
python -m pytest tests/test_login.py -v
```

### Run Specific Test
```bash
python -m pytest tests/test_login.py::TestLogin::test_successful_login -v
```

### Run Tests by Marker
```bash
python -m pytest -m smoke -v
python -m pytest -m critical -v
python -m pytest -m login -v
```

### Run Tests in Parallel
```bash
python -m pytest tests/ -n 4 -v
```

### Run with HTML Report Only
```bash
python -m pytest tests/test_login.py --html=reports/report.html --self-contained-html
```

## Viewing Reports

### HTML Report
Open: `reports/report.html` in your browser

### Allure Report
```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

## Configuration

Edit `.env` file to customize:
- `BASE_URL` - URL to test
- `BROWSER` - chromium, firefox, or webkit
- `HEADLESS` - true or false
- `TIMEOUT` - default timeout in milliseconds
- `SCREENSHOT_ON_FAILURE` - true or false

## Test Results Summary

**Latest Test Run:**
- Total Tests: 8
- Passed: 8 ✅
- Failed: 0
- Duration: ~25 seconds

**Test Cases:**
1. ✅ Successful login with valid credentials
2. ✅ Login with invalid username
3. ✅ Login with invalid password
4. ✅ Login with empty credentials
5. ✅ Login with empty username
6. ✅ Login with empty password
7. ✅ Logout functionality
8. ✅ Remember me checkbox

## Adding New Tests

1. Create test file in `tests/` directory
2. Import necessary page objects from `pages/`
3. Use fixtures from `conftest.py`
4. Add Allure decorators for reporting
5. Run tests and generate reports

## Framework Features

- **Page Object Model** - Maintainable and reusable page classes
- **Allure Reporting** - Beautiful test reports with steps and screenshots
- **Screenshot on Failure** - Automatic screenshot capture when tests fail
- **Parallel Execution** - Run tests faster with pytest-xdist
- **Configurable** - Easy configuration through .env file
- **Logging** - Comprehensive logging for debugging
- **Test Data Helpers** - Generate random test data easily

## Next Steps

1. Add more test cases for different features
2. Create page objects for other pages
3. Integrate with CI/CD pipeline
4. Add API testing capabilities
5. Implement data-driven testing

## Troubleshooting

**Issue:** Tests fail to find elements
**Solution:** Check selectors in page objects, ensure demo_login.html is accessible

**Issue:** Allure report not generating
**Solution:** Ensure allure command-line tool is installed and in PATH

**Issue:** Browser not launching
**Solution:** Run `playwright install` to install browser binaries

## Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review test logs in console output
3. Check screenshots in `screenshots/` directory
4. Review Allure report for detailed test steps
