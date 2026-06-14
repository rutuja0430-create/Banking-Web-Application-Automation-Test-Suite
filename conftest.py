import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import config

@pytest.fixture(scope='module')
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)  # Wait up to 10s for elements to appear
    driver.get(config.BASE_URL)
    yield driver
    driver.quit()