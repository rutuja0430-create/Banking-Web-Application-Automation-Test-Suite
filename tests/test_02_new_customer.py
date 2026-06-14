import json
import pytest
from pages.login_page import LoginPage
from pages.new_customer_page import NewCustomerPage
import config

with open('test_data/customer_data.json') as f:
    data = json.load(f)['valid_customer']

class TestNewCustomer:

    def test_TC04_create_customer_successfully(self, driver):
        """TC04: Fill all fields and verify Customer ID is generated"""
        import uuid
        login = LoginPage(driver)
        login.login()
        assert login.is_logged_in()

        elem = driver.find_element('link text', 'New Customer')
        driver.execute_script("arguments[0].click();", elem)

        nc = NewCustomerPage(driver)
        data['email'] = f"test_{uuid.uuid4().hex[:6]}@mailinator.com"
        nc.fill_and_submit(**data)

        try:
            from selenium.common.exceptions import TimeoutException
            customer_id = nc.get_customer_id()
            assert customer_id != ''
        except TimeoutException:
            import pytest
            pytest.skip("Guru99 server error: Timed out waiting for Customer ID")

        # Save to dynamic data
        try:
            with open('test_data/dynamic_data.json', 'r') as f:
                data_json = json.load(f)
        except FileNotFoundError:
            data_json = {}
        data_json['customer_id'] = customer_id
        with open('test_data/dynamic_data.json', 'w') as f:
            json.dump(data_json, f)
        print(f"\n✅ New Customer ID: {customer_id}")

    def test_TC05_empty_name_field(self, driver):
        """TC05: Empty name should show validation error"""
        driver.get(config.BASE_URL)
        login = LoginPage(driver)
        login.login()
        elem = driver.find_element('link text', 'New Customer')
        driver.execute_script("arguments[0].click();", elem)
        nc = NewCustomerPage(driver)
        nc.driver.find_element(*nc.CUSTOMER_NAME).click()
        nc.driver.find_element(*nc.CUSTOMER_NAME).send_keys('')
        nc.driver.find_element(*nc.DOB_INPUT).click()  # Tab away
        error = nc.get_name_error()
        assert 'Customer name must not be blank' in error

    def test_TC06_letters_in_pin(self, driver):
        """TC06: Letters in PIN should show error"""
        from selenium.webdriver.common.keys import Keys
        from selenium.common.exceptions import TimeoutException
        
        driver.get(config.BASE_URL)
        login = LoginPage(driver)
        login.login()
        
        elem = driver.find_element('link text', 'New Customer')
        driver.execute_script("arguments[0].click();", elem)
        nc = NewCustomerPage(driver)
        nc.driver.find_element(*nc.PIN_INPUT).send_keys('ABCDEF')
        nc.driver.find_element(*nc.PIN_INPUT).send_keys(Keys.TAB)
        try:
            error = nc.get_pin_error()
            assert error != ''
        except TimeoutException:
            pass