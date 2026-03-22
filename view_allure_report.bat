@echo off
REM Allure Report Viewer
REM This script generates and opens the Allure report

echo ========================================
echo    Allure Report Generator
echo ========================================
echo.

REM Check if allure-results directory exists
if not exist "reports\allure-results" (
    echo ERROR: No test results found!
    echo Please run tests first: python -m pytest tests/test_login.py
    echo.
    pause
    exit /b 1
)

echo Generating Allure report...
allure generate reports/allure-results --clean -o reports/allure-report

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Report generated successfully!
    echo Opening report in browser...
    echo.
    allure open reports/allure-report
) else (
    echo.
    echo ERROR: Failed to generate Allure report
    echo Make sure Allure is installed: https://docs.qameta.io/allure/
    echo.
    pause
)
