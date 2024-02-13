import data
import configuration
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestEnterProfile:
    def test_enter_profile_authorized_user_success(self, driver, reg_correct_user):
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
        profile = driver.current_url
        assert profile == configuration.MAIN_PAGE+configuration.PROFILE_PAGE
