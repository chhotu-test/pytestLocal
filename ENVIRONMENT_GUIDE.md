# Running Tests on Different Environments

## Environment Configuration

The framework supports three environments:
- **PreProd**: https://preprod-apps.abacus.ai
- **Production**: https://apps.abacus.ai
- **Staging**: https://staging-apps.abacus.ai

## Quick Start

### View Current Configuration
```bash
python show_config.py
```

### Method 1: Using Batch Script (Recommended for Windows)
```bash
run_tests_by_env.bat
```
This will show a menu to select the environment.

### Method 2: Using Command Line

#### Run on PreProd (Default)
```bash
python -m pytest tests/test_login.py --env=preprod -v
```

#### Run on Production
```bash
python -m pytest tests/test_login.py --env=prod -v
```

#### Run on Staging
```bash
python -m pytest tests/test_login.py --env=staging -v
```

## Advanced Options

### Run with Different Browser
```bash
# Firefox
python -m pytest tests/test_login.py --env=preprod --browser-type=firefox -v

# WebKit (Safari)
python -m pytest tests/test_login.py --env=preprod --browser-type=webkit -v
```

### Run in Headless Mode
```bash
python -m pytest tests/test_login.py --env=preprod --headless-mode=true -v
```

### Run Specific Test
```bash
python -m pytest tests/test_login.py::TestLogin::test_successful_login --env=preprod -v
```

### Run by Marker
```bash
# Smoke tests on production
python -m pytest -m smoke --env=prod -v

# Critical tests on staging
python -m pytest -m critical --env=staging -v
```

### Run in Parallel
```bash
python -m pytest tests/ --env=preprod -n 4 -v
```

## Setting Default Environment

Edit `.env` file and change:
```env
ENV=preprod
```

Options: `preprod`, `prod`, `staging`

## Test Credentials

Update your credentials in `.env` file:
```env
VALID_USERNAME=your_username
VALID_PASSWORD=your_password
```

## Examples

### Full Test Suite on PreProd
```bash
python -m pytest tests/test_login.py --env=preprod -v
```

### Smoke Tests on Production (Headless)
```bash
python -m pytest -m smoke --env=prod --headless-mode=true -v
```

### Single Test on Staging with Firefox
```bash
python -m pytest tests/test_login.py::TestLogin::test_successful_login --env=staging --browser-type=firefox -v
```

### All Tests in Parallel on PreProd
```bash
python -m pytest tests/ --env=preprod -n 4 -v
```

## Viewing Reports

### HTML Report
```bash
start reports/report.html
```

### Allure Report
```bash
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report
```

Or use:
```bash
view_allure_report.bat
```

## Troubleshooting

### Environment not switching
- Make sure to use `--env=` flag when running tests
- Check `.env` file for default environment setting

### Tests failing on real environment
- Verify credentials in `.env` file
- Check if the URL is accessible
- Ensure you have proper access to the environment
- Update page selectors if the UI has changed

### Browser not visible
- Set `HEADLESS=false` in `.env` file
- Or use `--headless-mode=false` flag

## Configuration Priority

1. Command line arguments (highest priority)
2. `.env` file settings
3. Default values in `config.py` (lowest priority)
