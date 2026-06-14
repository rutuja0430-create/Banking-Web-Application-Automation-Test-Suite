from selenium.webdriver.common.by import By

class FundTransferPage:
    PAYERS_ACC   = (By.NAME, 'payersaccount')
    PAYEES_ACC   = (By.NAME, 'payeeaccount')
    AMOUNT       = (By.NAME, 'ammount')
    DESCRIPTION  = (By.NAME, 'desc')
    SUBMIT       = (By.NAME, 'AccSubmit')
    SUCCESS_MSG  = (By.XPATH, "//*[contains(text(),'Fund Transfer successfully') or contains(text(),'Fund Transfer Details')]")
    ERROR_MSG    = (By.XPATH, "//p[contains(text(),'does not exist')]")

    def __init__(self, driver):
        self.driver = driver

    def transfer(self, from_acc, to_acc, amount, description='Test Transfer'):
        self.driver.find_element(*self.PAYERS_ACC).send_keys(from_acc)
        self.driver.find_element(*self.PAYEES_ACC).send_keys(to_acc)
        self.driver.find_element(*self.AMOUNT).send_keys(amount)
        self.driver.find_element(*self.DESCRIPTION).send_keys(description)
        self.driver.find_element(*self.SUBMIT).click()

    def is_transfer_successful(self):
        return len(self.driver.find_elements(*self.SUCCESS_MSG)) > 0

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