import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    ENV = os.getenv("ENV", "preprod").lower()

    ENVIRONMENTS = {
        "preprod": "https://support.orangehrm.com/portal/en/signin",
        "prod": "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
        "staging": "https://staging-apps.abacus.ai"
    }

    BASE_URL = ENVIRONMENTS.get(ENV, ENVIRONMENTS["preprod"])

    BROWSER = os.getenv("BROWSER", "chromium")

    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    SLOW_MO = int(os.getenv("SLOW_MO", "500"))

    TIMEOUT = int(os.getenv("TIMEOUT", "30000"))

    SCREENSHOT_ON_FAILURE = os.getenv("SCREENSHOT_ON_FAILURE", "true").lower() == "true"

    VIDEO_ON_FAILURE = os.getenv("VIDEO_ON_FAILURE", "false").lower() == "true"

    VIEWPORT_WIDTH = int(os.getenv("VIEWPORT_WIDTH", "1920"))
    VIEWPORT_HEIGHT = int(os.getenv("VIEWPORT_HEIGHT", "1080"))

    PARALLEL_WORKERS = int(os.getenv("PARALLEL_WORKERS", "1"))

    VALID_USERNAME = os.getenv("VALID_USERNAME", "testuser")
    VALID_PASSWORD = os.getenv("VALID_PASSWORD", "testpass123")

    INVALID_USERNAME = os.getenv("INVALID_USERNAME", "invaliduser")
    INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "wrongpass")

    ALLURE_RESULTS_DIR = os.getenv("ALLURE_RESULTS_DIR", "reports/allure-results")
    ALLURE_REPORT_DIR = os.getenv("ALLURE_REPORT_DIR", "reports/allure-report")

    SCREENSHOTS_DIR = os.getenv("SCREENSHOTS_DIR", "screenshots")
    VIDEOS_DIR = os.getenv("VIDEOS_DIR", "videos")

    @classmethod
    def get_browser_config(cls):
        return {
            "headless": cls.HEADLESS,
            "slow_mo": cls.SLOW_MO,
            "args": ["--start-maximized"] if not cls.HEADLESS else []
        }

    @classmethod
    def get_context_config(cls):
        config = {
            "record_video_dir": cls.VIDEOS_DIR if cls.VIDEO_ON_FAILURE else None
        }
        if cls.HEADLESS:
            config["viewport"] = {"width": cls.VIEWPORT_WIDTH, "height": cls.VIEWPORT_HEIGHT}
        else:
            config["no_viewport"] = True
        return config

    @classmethod
    def get_environment_url(cls, env: str = None):
        """Get URL for specific environment"""
        if env:
            return cls.ENVIRONMENTS.get(env.lower(), cls.BASE_URL)
        return cls.BASE_URL

    @classmethod
    def set_environment(cls, env: str):
        """Set the current environment"""
        if env.lower() in cls.ENVIRONMENTS:
            cls.ENV = env.lower()
            cls.BASE_URL = cls.ENVIRONMENTS[cls.ENV]
            return True
        return False

    @classmethod
    def get_all_environments(cls):
        """Get list of all available environments"""
        return list(cls.ENVIRONMENTS.keys())
