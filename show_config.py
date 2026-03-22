"""
Environment Configuration Display and Test Runner
Shows current configuration and allows running tests on different environments
"""
from config.config import Config
import sys
import os

def display_config():
    """Display current configuration"""
    print("=" * 70)
    print("Current Test Configuration")
    print("=" * 70)
    print(f"Environment: {Config.ENV.upper()}")
    print(f"Base URL: {Config.BASE_URL}")
    print(f"Browser: {Config.BROWSER}")
    print(f"Headless: {Config.HEADLESS}")
    print(f"Slow Motion: {Config.SLOW_MO}ms")
    print(f"Timeout: {Config.TIMEOUT}ms")
    print(f"Viewport: {Config.VIEWPORT_WIDTH}x{Config.VIEWPORT_HEIGHT}")
    print(f"Screenshot on Failure: {Config.SCREENSHOT_ON_FAILURE}")
    print("=" * 70)
    print()

def display_environments():
    """Display all available environments"""
    print("Available Environments:")
    print("-" * 70)
    for env, url in Config.ENVIRONMENTS.items():
        current = " (CURRENT)" if env == Config.ENV else ""
        print(f"  {env.upper()}: {url}{current}")
    print("-" * 70)
    print()

def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("UI Test Framework - Environment Configuration")
    print("=" * 70)
    print()
    
    display_config()
    display_environments()
    
    print("Usage Examples:")
    print("-" * 70)
    print("Run tests on PreProd:")
    print("  python -m pytest tests/test_login.py --env=preprod -v")
    print()
    print("Run tests on Production:")
    print("  python -m pytest tests/test_login.py --env=prod -v")
    print()
    print("Run tests on Staging:")
    print("  python -m pytest tests/test_login.py --env=staging -v")
    print()
    print("Run with different browser:")
    print("  python -m pytest tests/test_login.py --env=preprod --browser-type=firefox -v")
    print()
    print("Run in headless mode:")
    print("  python -m pytest tests/test_login.py --env=preprod --headless-mode=true -v")
    print()
    print("Or use the batch script:")
    print("  run_tests_by_env.bat")
    print("-" * 70)
    print()
    
    print("To change default environment, edit .env file and set:")
    print("  ENV=preprod  (or prod, or staging)")
    print("=" * 70)

if __name__ == "__main__":
    main()
