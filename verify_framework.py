"""
Framework Verification Script
Verifies that all components of the UI testing framework are properly set up
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists"""
    if os.path.exists(filepath):
        print(f"✅ {description}: {filepath}")
        return True
    else:
        print(f"❌ {description}: {filepath} - NOT FOUND")
        return False

def check_directory_exists(dirpath, description):
    """Check if a directory exists"""
    if os.path.isdir(dirpath):
        print(f"✅ {description}: {dirpath}")
        return True
    else:
        print(f"❌ {description}: {dirpath} - NOT FOUND")
        return False

def verify_framework():
    """Verify all framework components"""
    print("=" * 70)
    print("UI Testing Framework - Verification")
    print("=" * 70)
    print()
    
    all_checks_passed = True
    
    print("📁 Checking Directory Structure...")
    print("-" * 70)
    directories = [
        ("tests", "Test directory"),
        ("pages", "Page objects directory"),
        ("utils", "Utilities directory"),
        ("config", "Configuration directory"),
        ("reports", "Reports directory"),
        ("screenshots", "Screenshots directory"),
    ]
    
    for dir_name, description in directories:
        if not check_directory_exists(dir_name, description):
            all_checks_passed = False
    
    print()
    print("📄 Checking Core Files...")
    print("-" * 70)
    core_files = [
        ("conftest.py", "Pytest fixtures"),
        ("pytest.ini", "Pytest configuration"),
        ("requirements.txt", "Python dependencies"),
        (".env", "Environment configuration"),
        (".gitignore", "Git ignore rules"),
    ]
    
    for file_name, description in core_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("📦 Checking Page Objects...")
    print("-" * 70)
    page_files = [
        ("pages/__init__.py", "Pages package init"),
        ("pages/base_page.py", "Base page class"),
        ("pages/login_page.py", "Login page object"),
    ]
    
    for file_name, description in page_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("🧪 Checking Test Files...")
    print("-" * 70)
    test_files = [
        ("tests/__init__.py", "Tests package init"),
        ("tests/test_login.py", "Login test cases"),
    ]
    
    for file_name, description in test_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("🛠️ Checking Utilities...")
    print("-" * 70)
    util_files = [
        ("utils/__init__.py", "Utils package init"),
        ("utils/logger.py", "Logger utility"),
        ("utils/screenshot_helper.py", "Screenshot helper"),
        ("utils/test_data_helper.py", "Test data helper"),
    ]
    
    for file_name, description in util_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("⚙️ Checking Configuration...")
    print("-" * 70)
    config_files = [
        ("config/__init__.py", "Config package init"),
        ("config/config.py", "Configuration management"),
    ]
    
    for file_name, description in config_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("📚 Checking Documentation...")
    print("-" * 70)
    doc_files = [
        ("README.md", "Main documentation"),
        ("QUICK_START.md", "Quick start guide"),
        ("RUNNING_TESTS.md", "Test execution guide"),
        ("SETUP_COMPLETE.md", "Setup completion summary"),
    ]
    
    for file_name, description in doc_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("🚀 Checking Batch Scripts...")
    print("-" * 70)
    batch_files = [
        ("run_all_tests.bat", "Run all tests script"),
        ("run_login_tests.bat", "Run individual tests script"),
        ("view_allure_report.bat", "View Allure report script"),
    ]
    
    for file_name, description in batch_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("🌐 Checking Demo Files...")
    print("-" * 70)
    demo_files = [
        ("demo_login.html", "Demo login page"),
        ("forgot-password.html", "Demo forgot password page"),
    ]
    
    for file_name, description in demo_files:
        if not check_file_exists(file_name, description):
            all_checks_passed = False
    
    print()
    print("=" * 70)
    if all_checks_passed:
        print("✅ ALL CHECKS PASSED - Framework is ready!")
    else:
        print("❌ SOME CHECKS FAILED - Please review the output above")
    print("=" * 70)
    print()
    
    print("📊 Framework Statistics:")
    print("-" * 70)
    print(f"Total Directories: {len(directories)}")
    print(f"Total Files: {len(core_files) + len(page_files) + len(test_files) + len(util_files) + len(config_files) + len(doc_files) + len(batch_files) + len(demo_files)}")
    print(f"Test Cases: 8")
    print(f"Page Objects: 2 (BasePage, LoginPage)")
    print(f"Utilities: 3 (Logger, ScreenshotHelper, TestDataHelper)")
    print()
    
    print("🎯 Next Steps:")
    print("-" * 70)
    print("1. Run tests: python -m pytest tests/test_login.py -v")
    print("2. View HTML report: start reports/report.html")
    print("3. Generate Allure report: allure generate reports/allure-results -o reports/allure-report")
    print("4. View Allure report: allure open reports/allure-report")
    print("5. Read documentation: README.md, QUICK_START.md")
    print()
    
    return all_checks_passed

if __name__ == "__main__":
    success = verify_framework()
    sys.exit(0 if success else 1)
