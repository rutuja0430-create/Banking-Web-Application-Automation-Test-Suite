from selenium.webdriver.common.by import By

class BalanceEnquiryPage:
    ACCOUNT_NO  = (By.NAME, 'accountno')
    SUBMIT      = (By.NAME, 'AccSubmit')
    BALANCE     = (By.XPATH, "//td[text()='Balance']/following-sibling::td")

    def __init__(self, driver):
        self.driver = driver

    def check_balance(self, account_no):
        self.driver.find_element(*self.ACCOUNT_NO).clear()
        self.driver.find_element(*self.ACCOUNT_NO).send_keys(account_no)
        self.driver.find_element(*self.SUBMIT).click()

    def get_balance(self):
        return self.driver.find_element(*self.BALANCE).text

    def get_error_message(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            msg = alert.text
            alert.accept()
            return msg
        except TimeoutException:
            return "No alert present - possible server 500 error"