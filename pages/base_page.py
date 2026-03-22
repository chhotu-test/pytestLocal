import os
from datetime import datetime
from playwright.sync_api import Page, expect
import allure


class BasePage:
    
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 30000
    
    @allure.step("Navigate to URL: {url}")
    def navigate(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")
    
    @allure.step("Click element: {selector}")
    def click(self, selector: str):
        self.page.locator(selector).click(timeout=self.timeout)
    
    @allure.step("Fill text '{text}' in element: {selector}")
    def fill(self, selector: str, text: str):
        self.page.locator(selector).fill(text, timeout=self.timeout)
    
    @allure.step("Get text from element: {selector}")
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content(timeout=self.timeout)
    
    @allure.step("Check if element is visible: {selector}")
    def is_visible(self, selector: str) -> bool:
        try:
            return self.page.locator(selector).is_visible(timeout=5000)
        except:
            return False
    
    @allure.step("Wait for element: {selector}")
    def wait_for_element(self, selector: str):
        self.page.locator(selector).wait_for(state="visible", timeout=self.timeout)
    
    @allure.step("Wait for URL to contain: {url_part}")
    def wait_for_url(self, url_part: str):
        self.page.wait_for_url(f"**/*{url_part}*", timeout=self.timeout)
    
    @allure.step("Take screenshot")
    def take_screenshot(self, name: str = None):
        if name is None:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        
        self.page.screenshot(path=screenshot_path, full_page=True)
        allure.attach.file(screenshot_path, name=name, attachment_type=allure.attachment_type.PNG)
        return screenshot_path
    
    @allure.step("Get current URL")
    def get_current_url(self) -> str:
        return self.page.url
    
    @allure.step("Get page title")
    def get_title(self) -> str:
        return self.page.title()
    
    @allure.step("Press key: {key}")
    def press_key(self, selector: str, key: str):
        self.page.locator(selector).press(key)
    
    @allure.step("Select option: {value}")
    def select_option(self, selector: str, value: str):
        self.page.locator(selector).select_option(value)
    
    @allure.step("Check checkbox: {selector}")
    def check(self, selector: str):
        self.page.locator(selector).check()
    
    @allure.step("Uncheck checkbox: {selector}")
    def uncheck(self, selector: str):
        self.page.locator(selector).uncheck()
    
    @allure.step("Hover over element: {selector}")
    def hover(self, selector: str):
        self.page.locator(selector).hover()
    
    @allure.step("Wait for {seconds} seconds")
    def wait(self, seconds: int):
        self.page.wait_for_timeout(seconds * 1000)
    
    @allure.step("Verify element contains text: {expected_text}")
    def verify_text(self, selector: str, expected_text: str):
        expect(self.page.locator(selector)).to_contain_text(expected_text, timeout=self.timeout)
    
    @allure.step("Verify element is visible: {selector}")
    def verify_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible(timeout=self.timeout)
    
    @allure.step("Verify element is hidden: {selector}")
    def verify_hidden(self, selector: str):
        expect(self.page.locator(selector)).to_be_hidden(timeout=self.timeout)
    
    @allure.step("Reload page")
    def reload(self):
        self.page.reload()
    
    @allure.step("Go back")
    def go_back(self):
        self.page.go_back()
    
    @allure.step("Go forward")
    def go_forward(self):
        self.page.go_forward()
