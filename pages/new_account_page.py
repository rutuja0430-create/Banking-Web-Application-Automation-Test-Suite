from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class NewAccountPage:
    CUSTOMER_ID    = (By.NAME, 'cusid')
    ACCOUNT_TYPE   = (By.NAME, 'selaccount')
    DEPOSIT        = (By.NAME, 'inideposit')
    SUBMIT_BUTTON  = (By.NAME, 'button2')
    ACCOUNT_ID     = (By.XPATH, "//td[text()='Account ID']/following-sibling::td")

    def __init__(self, driver):
        self.driver = driver

    def create_account(self, customer_id, account_type='Savings', deposit='5000'):
        self.driver.find_element(*self.CUSTOMER_ID).send_keys(customer_id)
        Select(self.driver.find_element(*self.ACCOUNT_TYPE)).select_by_visible_text(account_type)
        self.driver.find_element(*self.DEPOSIT).send_keys(deposit)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_account_id(self):
        return self.driver.find_element(*self.ACCOUNT_ID).text