import pytest
import configuration
import data
from selenium import webdriver
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
# используемые фикстуры

@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def reg_correct_user(driver):
    driver.get(configuration.MAIN_PAGE + configuration.REG_PAGE)
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.REG_BUTTON))
    driver.find_element(*TestLocators.REG_NAME).send_keys(data.registered_user['name'])
    driver.find_element(*TestLocators.REG_E_MAIL).send_keys(data.registered_user['e-mail'])
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys(data.registered_user['password'])
    driver.find_element(*TestLocators.REG_BUTTON).click()
    pass
