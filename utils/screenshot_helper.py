import os
from datetime import datetime
import allure
from playwright.sync_api import Page


class ScreenshotHelper:
    
    @staticmethod
    def capture_screenshot(page: Page, name: str = None, attach_to_allure: bool = True):
        if name is None:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        
        page.screenshot(path=screenshot_path, full_page=True)
        
        if attach_to_allure:
            allure.attach.file(
                screenshot_path,
                name=name,
                attachment_type=allure.attachment_type.PNG
            )
        
        return screenshot_path
    
    @staticmethod
    def capture_element_screenshot(page: Page, selector: str, name: str = None):
        if name is None:
            name = f"element_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{name}.png")
        
        element = page.locator(selector)
        element.screenshot(path=screenshot_path)
        
        allure.attach.file(
            screenshot_path,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
        
        return screenshot_path
