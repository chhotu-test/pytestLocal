@echo off
echo ========================================
echo Running Login Tests
echo ========================================
echo.

echo Choose an option:
echo 1. Run ALL login tests
echo 2. Run ONLY successful login test
echo 3. Run ONLY invalid username test
echo 4. Run ONLY invalid password test
echo 5. Run ONLY empty credentials test
echo 6. Run ONLY logout test
echo 7. Run SMOKE tests only
echo 8. Run and generate Allure report
echo.

set /p choice="Enter your choice (1-8): "

if "%choice%"=="1" (
    echo Running all login tests...
    pytest tests/test_login.py -v -s
) else if "%choice%"=="2" (
    echo Running successful login test...
    pytest tests/test_login.py::TestLogin::test_successful_login -v -s
) else if "%choice%"=="3" (
    echo Running invalid username test...
    pytest tests/test_login.py::TestLogin::test_login_invalid_username -v -s
) else if "%choice%"=="4" (
    echo Running invalid password test...
    pytest tests/test_login.py::TestLogin::test_login_invalid_password -v -s
) else if "%choice%"=="5" (
    echo Running empty credentials test...
    pytest tests/test_login.py::TestLogin::test_login_empty_credentials -v -s
) else if "%choice%"=="6" (
    echo Running logout test...
    pytest tests/test_login.py::TestLogin::test_logout -v -s
) else if "%choice%"=="7" (
    echo Running smoke tests...
    pytest tests/test_login.py -m smoke -v -s
) else if "%choice%"=="8" (
    echo Running all tests and generating Allure report...
    pytest tests/test_login.py -v -s
    echo.
    echo Generating Allure report...
    allure serve reports/allure-results
) else (
    echo Invalid choice!
)

echo.
pause
