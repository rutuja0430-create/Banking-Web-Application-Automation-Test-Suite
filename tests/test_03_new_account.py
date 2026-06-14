import pytest
from pages.login_page import LoginPage
from pages.new_account_page import NewAccountPage
import config
import json



class TestNewAccount:

    def test_TC07_create_savings_account(self, driver):
        """TC07: Create savings account — should generate Account ID"""
        login = LoginPage(driver)
        login.login()
        elem = driver.find_element('link text', 'New Account')
        driver.execute_script("arguments[0].click();", elem)

        try:
            with open('test_data/dynamic_data.json', 'r') as f:
                customer_id = json.load(f).get('customer_id', '69669')
        except FileNotFoundError:
            customer_id = '69669'

        na = NewAccountPage(driver)
        na.create_account(customer_id, account_type='Savings', deposit='5000')
        account_id = na.get_account_id()
        assert account_id != ''
        try:
            with open('test_data/dynamic_data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        data['account_1'] = account_id
        with open('test_data/dynamic_data.json', 'w') as f:
            json.dump(data, f)
        print(f"\n✅ Savings Account ID: {account_id}")

    def test_TC08_create_current_account(self, driver):
        """TC08: Create current account — should generate Account ID"""
        elem = driver.find_element('link text', 'New Account')
        driver.execute_script("arguments[0].click();", elem)
        try:
            with open('test_data/dynamic_data.json', 'r') as f:
                customer_id = json.load(f).get('customer_id', '69669')
        except FileNotFoundError:
            customer_id = '69669'

        na = NewAccountPage(driver)
        na.create_account(customer_id, account_type='Current', deposit='5000')
        account_id = na.get_account_id()
        assert account_id != ''
        try:
            with open('test_data/dynamic_data.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}
        data['account_2'] = account_id
        with open('test_data/dynamic_data.json', 'w') as f:
            json.dump(data, f)
        print(f"\n✅ Current Account ID: {account_id}")