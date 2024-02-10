import data
import configuration
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogIn:
    def test_login_through_button_login(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_ACC_BUTTON))
        driver.find_element(*TestLocators.LOGIN_ACC_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        order = driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text
        driver.quit()
        assert order == 'Оформить заказ'

    def test_login_through_profile_button(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_ACC_BUTTON))
        driver.find_element(*TestLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        order = driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text
        driver.quit()
        assert order == 'Оформить заказ'

    def test_login_through_registration_form_link(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE+configuration.REG_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.REG_BUTTON))
        driver.find_element(*TestLocators.ENTER_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        order = driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text
        driver.quit()
        assert order == 'Оформить заказ'

    def test_login_through_forgot_password_link(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE+configuration.FORGOT_PASSWORD)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.RESTORE_BUTTON))
        driver.find_element(*TestLocators.ENTER_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        order = driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text
        driver.quit()
        assert order == 'Оформить заказ'

    def test_login_through_reset_password_link(self, driver, reg_correct_user):
        driver.get(configuration.MAIN_PAGE + configuration.FORGOT_PASSWORD)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.RESTORE_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.RESTORE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.SAVE_BUTTON))
        driver.find_element(*TestLocators.ENTER_LINK).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        driver.find_element(*TestLocators.LOGIN_E_MAIL).send_keys(data.registered_user['e-mail'])
        driver.find_element(*TestLocators.LOGIN_PASSWORD).send_keys(data.registered_user['password'])
        driver.find_element(*TestLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.MAKE_ORDER_BUTTON))
        order = driver.find_element(*TestLocators.MAKE_ORDER_BUTTON).text
        driver.quit()
        assert order == 'Оформить заказ'
