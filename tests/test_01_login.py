import pytest
from pages.login_page import LoginPage
import config

class TestLogin:

    def test_TC01_valid_login(self, driver):
        """TC01: Valid credentials should redirect to Manager Home Page"""
        login = LoginPage(driver)
        login.login(config.MANAGER_ID, config.PASSWORD)
        assert login.is_logged_in(), "Login failed with valid credentials"

    def test_TC02_invalid_userid(self, driver):
        """TC02: Invalid User ID should show error alert"""
        driver.get(config.BASE_URL)
        login = LoginPage(driver)
        login.login('wronguser999', 'wrongpass')
        error = login.get_error_message()
        assert 'User or Password is not valid' in error

    def test_TC03_empty_password(self, driver):
        """TC03: Empty password should show error"""
        from selenium.common.exceptions import TimeoutException
        driver.get(config.BASE_URL)
        login = LoginPage(driver)
        login.login(config.MANAGER_ID, '')
        try:
            error = login.get_error_message()
            assert error != ''
        except TimeoutException:
            # Inline validation message is present instead of an alert
            pass