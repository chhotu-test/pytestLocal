@echo off
REM Complete Test Execution Script
REM Runs all tests and generates both HTML and Allure reports

echo ========================================
echo    UI Test Framework - Full Run
echo ========================================
echo.

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call .venv\Scripts\activate.bat
    echo.
)

echo Running all login tests...
echo.
python -m pytest tests/test_login.py -v

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo    All Tests Passed! ✓
    echo ========================================
    echo.
) else (
    echo.
    echo ========================================
    echo    Some Tests Failed! ✗
    echo ========================================
    echo.
)

echo Generating Allure report...
allure generate reports/allure-results --clean -o reports/allure-report

echo.
echo ========================================
echo    Reports Generated
echo ========================================
echo.
echo HTML Report: reports\report.html
echo Allure Report: reports\allure-report\index.html
echo.
echo To view Allure report, run: allure open reports/allure-report
echo.

pause
