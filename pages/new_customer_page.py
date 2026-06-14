from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NewCustomerPage:
    CUSTOMER_NAME  = (By.NAME, 'name')
    DOB_INPUT      = (By.NAME, 'dob')
    ADDRESS        = (By.NAME, 'addr')
    CITY           = (By.NAME, 'city')
    STATE          = (By.NAME, 'state')
    PIN_INPUT      = (By.NAME, 'pinno')
    MOBILE         = (By.NAME, 'telephoneno')
    EMAIL          = (By.NAME, 'emailid')
    PASSWORD       = (By.NAME, 'password')
    SUBMIT_BUTTON  = (By.NAME, 'sub')
    CUSTOMER_ID    = (By.XPATH, "//td[text()='Customer ID']/following-sibling::td")
    NAME_ERROR     = (By.ID, 'message')
    PIN_ERROR      = (By.ID, 'message2')  # ← correct ID for PIN error

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_and_submit(self, name, dob, address, city, state, pin, mobile, email, password):
        self.wait.until(EC.presence_of_element_located(self.CUSTOMER_NAME))
        self.driver.find_element(*self.CUSTOMER_NAME).clear()
        self.driver.find_element(*self.CUSTOMER_NAME).send_keys(name)
        self.driver.find_element(*self.DOB_INPUT).send_keys(dob)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.PIN_INPUT).send_keys(pin)
        self.driver.find_element(*self.MOBILE).send_keys(mobile)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_customer_id(self):
        self.wait.until(EC.presence_of_element_located(self.CUSTOMER_ID))
        return self.driver.find_element(*self.CUSTOMER_ID).text

    def get_name_error(self):
        self.wait.until(EC.presence_of_element_located(self.NAME_ERROR))
        return self.driver.find_element(*self.NAME_ERROR).text

    def get_pin_error(self):
        self.wait.until(EC.presence_of_element_located(self.PIN_ERROR))
        return self.driver.find_element(*self.PIN_ERROR).text