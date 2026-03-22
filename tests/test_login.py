import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Authentication")
@allure.suite("Login Tests")
class TestLogin:
    
    @allure.title("Test successful login with valid credentials")
    @allure.description("Verify that user can login successfully with valid username and password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.critical
    def test_successful_login(self, login_page, base_url, valid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Verify login page is loaded"):
            login_page.verify_login_page_loaded()
        
        with allure.step("Perform login with valid credentials"):
            login_page.login(
                valid_credentials["username"],
                valid_credentials["password"]
            )
        
        with allure.step("Verify successful login"):
            login_page.verify_successful_login()
        
        with allure.step("Take screenshot of successful login"):
            login_page.take_screenshot("successful_login")
    
    @allure.title("Test login with invalid username")
    @allure.description("Verify that login fails with invalid username")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_invalid_username(self, login_page, base_url, invalid_credentials, valid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Attempt login with invalid username"):
            login_page.login(
                invalid_credentials["username"],
                valid_credentials["password"]
            )
        
        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed(), "Error message should be displayed"
        
        with allure.step("Take screenshot of error"):
            login_page.take_screenshot("invalid_username_error")
    
    @allure.title("Test login with invalid password")
    @allure.description("Verify that login fails with invalid password")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.login
    def test_login_invalid_password(self, login_page, base_url, valid_credentials, invalid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Attempt login with invalid password"):
            login_page.login(
                valid_credentials["username"],
                invalid_credentials["password"]
            )
        
        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed(), "Error message should be displayed"
    
    @allure.title("Test login with empty credentials")
    @allure.description("Verify that login fails when username and password are empty")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_empty_credentials(self, login_page, base_url):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Attempt login with empty credentials"):
            login_page.login("", "")
        
        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed(), "Error message should be displayed"
    
    @allure.title("Test login with empty username")
    @allure.description("Verify that login fails when username is empty")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_empty_username(self, login_page, base_url, valid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Attempt login with empty username"):
            login_page.login("", valid_credentials["password"])
        
        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed(), "Error message should be displayed"
    
    @allure.title("Test login with empty password")
    @allure.description("Verify that login fails when password is empty")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.login
    def test_login_empty_password(self, login_page, base_url, valid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Attempt login with empty password"):
            login_page.login(valid_credentials["username"], "")
        
        with allure.step("Verify error message is displayed"):
            assert login_page.is_error_message_displayed(), "Error message should be displayed"
    
    @allure.title("Test logout functionality")
    @allure.description("Verify that user can logout successfully after login")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.login
    def test_logout(self, login_page, base_url, valid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)
        
        with allure.step("Login with valid credentials"):
            login_page.login(
                valid_credentials["username"],
                valid_credentials["password"]
            )
        
        with allure.step("Verify successful login"):
            login_page.verify_successful_login()
        
        with allure.step("Perform logout"):
            login_page.logout()
        
        with allure.step("Verify user is logged out"):
            login_page.verify_login_page_loaded()
    
    @allure.title("Test remember me functionality")
    @allure.description("Verify that remember me checkbox works correctly")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    @pytest.mark.login
    def test_remember_me(self, login_page, base_url, valid_credentials):
        with allure.step("Open login page"):
            login_page.open_login_page(base_url)

        with allure.step("Check remember me checkbox"):
            login_page.check_remember_me()

        with allure.step("Login with valid credentials"):
            login_page.login(
                valid_credentials["username"],
                valid_credentials["password"]
            )

        with allure.step("Verify successful login"):
            login_page.verify_successful_login()


@allure.feature("Authentication")
@allure.suite("Login Steps Tests")
class TestLoginSteps:

    @allure.title("Test login step: {step_name}")
    @pytest.mark.login
    @pytest.mark.parametrize("step_name, action", [
        ("open_login_page", "open_login_page"),
        ("enter_username", "enter_username"),
        ("enter_password", "enter_password"),
        ("click_login_button", "click_login_button"),
    ])
    def test_login_step(self, login_page, base_url, valid_credentials, step_name, action):
        login_page.open_login_page(base_url)

        if action == "open_login_page":
            with allure.step("Verify login page is loaded"):
                login_page.verify_login_page_loaded()

        elif action == "enter_username":
            with allure.step("Enter username"):
                login_page.enter_username(valid_credentials["username"])

        elif action == "enter_password":
            with allure.step("Enter password"):
                login_page.enter_password(valid_credentials["password"])

        elif action == "click_login_button":
            with allure.step("Enter credentials and click login"):
                login_page.enter_username(valid_credentials["username"])
                login_page.enter_password(valid_credentials["password"])
                login_page.click_login_button()


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s", "--alluredir=reports/allure-results"])
