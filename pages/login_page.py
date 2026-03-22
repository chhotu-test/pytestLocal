from pages.base_page import BasePage
from playwright.sync_api import Page
import allure


class LoginPage(BasePage):
    
    def __init__(self, page: Page):
        super().__init__(page)
        
        self.username_input = "#username"
        self.password_input = "#password"
        self.login_button = "button[type='submit']"
        self.error_message = ".error-message"
        self.success_message = ".success-message"
        self.logout_button = "#logout"
        self.forgot_password_link = "a[href*='forgot-password']"
        self.remember_me_checkbox = "#remember-me"
        self.login_form = "form#login-form"
    
    @allure.step("Open login page")
    def open_login_page(self, url: str):
        self.navigate(url)
        self.wait_for_element(self.login_form)
    
    @allure.step("Enter username: {username}")
    def enter_username(self, username: str):
        self.fill(self.username_input, username)
    
    @allure.step("Enter password")
    def enter_password(self, password: str):
        self.fill(self.password_input, password)
    
    @allure.step("Click login button")
    def click_login_button(self):
        self.click(self.login_button)
    
    @allure.step("Perform login with username: {username}")
    def login(self, username: str, password: str):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    @allure.step("Check if error message is displayed")
    def is_error_message_displayed(self) -> bool:
        return self.is_visible(self.error_message)
    
    @allure.step("Get error message text")
    def get_error_message(self) -> str:
        return self.get_text(self.error_message)
    
    @allure.step("Check if success message is displayed")
    def is_success_message_displayed(self) -> bool:
        return self.is_visible(self.success_message)
    
    @allure.step("Get success message text")
    def get_success_message(self) -> str:
        return self.get_text(self.success_message)
    
    @allure.step("Check if logout button is displayed")
    def is_logout_button_displayed(self) -> bool:
        return self.is_visible(self.logout_button)
    
    @allure.step("Click logout button")
    def logout(self):
        self.click(self.logout_button)
    
    @allure.step("Click forgot password link")
    def click_forgot_password(self):
        self.click(self.forgot_password_link)
    
    @allure.step("Check remember me checkbox")
    def check_remember_me(self):
        self.check(self.remember_me_checkbox)
    
    @allure.step("Verify login page is loaded")
    def verify_login_page_loaded(self):
        self.verify_visible(self.login_form)
        self.verify_visible(self.username_input)
        self.verify_visible(self.password_input)
        self.verify_visible(self.login_button)
    
    @allure.step("Verify successful login")
    def verify_successful_login(self):
        self.verify_visible(self.logout_button)
    
    @allure.step("Clear login form")
    def clear_login_form(self):
        self.fill(self.username_input, "")
        self.fill(self.password_input, "")
