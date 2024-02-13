import data
import configuration
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMoveFromProfile:
    def test_leave_profile_for_constructor_through_constructor_bottom_success(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_ACC_BUTTON))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.SAVE_BUTTON))
        driver.find_element(*TestLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert driver.current_url == configuration.MAIN_PAGE

    def test_leave_profile_for_constructor_through_logo_success(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_ACC_BUTTON))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.SAVE_BUTTON))
        driver.find_element(*TestLocators.LOGO_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        assert driver.current_url == configuration.MAIN_PAGE
