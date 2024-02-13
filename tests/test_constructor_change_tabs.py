import configuration
from locators import TestLocators
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorTabs:

    def test_change_tabs_bulki_to_sous_in_constructor_success(self, driver):
        driver.get(configuration.MAIN_PAGE)
        driver.find_element(*TestLocators.TAB_SOUS).click()
        WebDriverWait(driver, 3)
        elem = driver.find_element(*TestLocators.TAB_SOUS)
        assert elem == driver.find_element(*TestLocators.CHOSEN_TAB)

    def test_change_tabs_bulki_to_nachinki_in_constructor_success(self, driver):
        driver.get(configuration.MAIN_PAGE)
        driver.find_element(*TestLocators.TAB_NACHINKI).click()
        WebDriverWait(driver, 3)
        elem = driver.find_element(*TestLocators.TAB_NACHINKI)
        assert elem == driver.find_element(*TestLocators.CHOSEN_TAB)

    def test_change_tabs_sous_to_bulki_in_constructor_success(self, driver):
        driver.get(configuration.MAIN_PAGE)
        driver.find_element(*TestLocators.TAB_SOUS).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.TAB_BULKI).click()
        WebDriverWait(driver, 3)
        elem = driver.find_element(*TestLocators.TAB_BULKI)
        assert elem == driver.find_element(*TestLocators.CHOSEN_TAB)

    def test_change_tabs_nachinki_to_bulki_in_constructor_success(self, driver):
        driver.get(configuration.MAIN_PAGE)
        driver.find_element(*TestLocators.TAB_NACHINKI).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.TAB_BULKI).click()
        WebDriverWait(driver, 3)
        elem = driver.find_element(*TestLocators.TAB_BULKI)
        assert elem == driver.find_element(*TestLocators.CHOSEN_TAB)

    def test_change_tabs_sous_to_nachinki_in_constructor_success(self, driver):
        driver.get(configuration.MAIN_PAGE)
        driver.find_element(*TestLocators.TAB_SOUS).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.TAB_NACHINKI).click()
        WebDriverWait(driver, 3)
        elem = driver.find_element(*TestLocators.TAB_NACHINKI)
        assert elem == driver.find_element(*TestLocators.CHOSEN_TAB)

    def test_change_tabs_nachinki_to_sous_in_constructor_success(self, driver):
        driver.get(configuration.MAIN_PAGE)
        driver.find_element(*TestLocators.TAB_NACHINKI).click()
        WebDriverWait(driver, 3)
        driver.find_element(*TestLocators.TAB_SOUS).click()
        WebDriverWait(driver, 3)
        elem = driver.find_element(*TestLocators.TAB_SOUS)
        assert elem == driver.find_element(*TestLocators.CHOSEN_TAB)
