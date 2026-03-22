@echo off
REM Environment-based Test Execution Script
REM Allows selection of environment (preprod, prod, staging) before running tests

echo ========================================
echo    UI Test Framework - Environment Selector
echo ========================================
echo.

REM Activate virtual environment if it exists
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

:MENU
echo.
echo Select Environment:
echo ========================================
echo 1. PreProd (https://preprod-apps.abacus.ai)
echo 2. Production (https://apps.abacus.ai)
echo 3. Staging (https://staging-apps.abacus.ai)
echo 4. Exit
echo ========================================
echo.

set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" (
    set ENV=preprod
    goto RUN_TESTS
)
if "%choice%"=="2" (
    set ENV=prod
    goto RUN_TESTS
)
if "%choice%"=="3" (
    set ENV=staging
    goto RUN_TESTS
)
if "%choice%"=="4" (
    echo Exiting...
    exit /b 0
)

echo Invalid choice! Please try again.
goto MENU

:RUN_TESTS
echo.
echo ========================================
echo Running tests on %ENV% environment
echo ========================================
echo.

REM Set environment variable
set ENV=%ENV%

REM Run tests
python -m pytest tests/test_login.py -v --env=%ENV%

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ========================================
    echo    All Tests Passed on %ENV%! ✓
    echo ========================================
) else (
    echo.
    echo ========================================
    echo    Some Tests Failed on %ENV%! ✗
    echo ========================================
)

echo.
echo Generating Allure report...
allure generate reports/allure-results --clean -o reports/allure-report

echo.
echo ========================================
echo    Reports Generated
echo ========================================
echo HTML Report: reports\report.html
echo Allure Report: reports\allure-report\index.html
echo.

pause
