from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import config

class LoginPage:
    USERID_INPUT   = (By.NAME, 'uid')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN_BUTTON   = (By.NAME, 'btnLogin')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, userid=config.MANAGER_ID, password=config.PASSWORD):
        self.driver.find_element(*self.USERID_INPUT).clear()
        self.driver.find_element(*self.USERID_INPUT).send_keys(userid)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        return 'Manager HomePage' in self.driver.title

    def get_error_message(self):
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        msg = alert.text
        alert.accept()
        return msg