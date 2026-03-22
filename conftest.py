import pytest
import allure
from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from config.config import Config
from datetime import datetime
import os


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="preprod",
        help="Environment to run tests against: preprod, prod, or staging"
    )
    parser.addoption(
        "--browser-type",
        action="store",
        default=None,
        help="Browser type: chromium, firefox, or webkit"
    )
    parser.addoption(
        "--headless-mode",
        action="store",
        default=None,
        help="Run in headless mode: true or false"
    )


@pytest.fixture(scope="session")
def environment(request):
    env = request.config.getoption("--env")
    if Config.set_environment(env):
        print(f"\n[OK] Running tests on {env.upper()} environment: {Config.BASE_URL}")
    else:
        print(f"\n[WARN] Invalid environment '{env}', using default: preprod")
    return env


@pytest.fixture(scope="session")
def browser_type_launch_args(request):
    browser_type = request.config.getoption("--browser-type")
    if browser_type:
        Config.BROWSER = browser_type

    headless = request.config.getoption("--headless-mode")
    if headless:
        Config.HEADLESS = headless.lower() == "true"

    return Config.get_browser_config()


@pytest.fixture(scope="session")
def browser_context_args():
    return Config.get_context_config()


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_type_launch_args, environment):
    browser_type = getattr(playwright_instance, Config.BROWSER)
    browser = browser_type.launch(**browser_type_launch_args)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser, browser_context_args):
    context = browser.new_context(**browser_context_args)
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(Config.TIMEOUT)
    yield page
    page.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        if report.failed:
            if Config.SCREENSHOT_ON_FAILURE:
                page = item.funcargs.get("page")
                if page:
                    try:
                        screenshot_dir = Config.SCREENSHOTS_DIR
                        os.makedirs(screenshot_dir, exist_ok=True)
                        
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        screenshot_name = f"{item.name}_{timestamp}"
                        screenshot_path = os.path.join(screenshot_dir, f"{screenshot_name}.png")
                        
                        page.screenshot(path=screenshot_path, full_page=True)
                        
                        allure.attach.file(
                            screenshot_path,
                            name=screenshot_name,
                            attachment_type=allure.attachment_type.PNG
                        )
                    except Exception as e:
                        print(f"Failed to capture screenshot: {e}")


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: Mark test as smoke test"
    )
    config.addinivalue_line(
        "markers", "regression: Mark test as regression test"
    )
    config.addinivalue_line(
        "markers", "login: Mark test as login functionality test"
    )
    config.addinivalue_line(
        "markers", "critical: Mark test as critical test"
    )
    
    os.makedirs(Config.ALLURE_RESULTS_DIR, exist_ok=True)
    os.makedirs(Config.SCREENSHOTS_DIR, exist_ok=True)
    if Config.VIDEO_ON_FAILURE:
        os.makedirs(Config.VIDEOS_DIR, exist_ok=True)


@pytest.fixture(scope="function")
def login_page(page):
    from pages.login_page import LoginPage
    return LoginPage(page)


@pytest.fixture(scope="session")
def base_url():
    return Config.BASE_URL


@pytest.fixture(scope="session")
def valid_credentials():
    return {
        "username": Config.VALID_USERNAME,
        "password": Config.VALID_PASSWORD
    }


@pytest.fixture(scope="session")
def invalid_credentials():
    return {
        "username": Config.INVALID_USERNAME,
        "password": Config.INVALID_PASSWORD
    }
