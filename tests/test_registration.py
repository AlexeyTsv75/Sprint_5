import time

import data
import configuration
from locators import TestLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:
    def test_registration_correct_user_success(self, driver):
        driver.get(configuration.MAIN_PAGE + configuration.REG_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.REG_BUTTON))
        driver.find_element(*TestLocators.REG_NAME).send_keys(data.new_correct_user['name'])
        driver.find_element(*TestLocators.REG_E_MAIL).send_keys(data.new_correct_user['e-mail'])
        driver.find_element(*TestLocators.REG_PASSWORD).send_keys(data.new_correct_user['password'])
        time.sleep(3)
        driver.find_element(*TestLocators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.LOGIN_BUTTON))
        assert driver.current_url == configuration.MAIN_PAGE + configuration.AUTHOR_PAGE
        driver.quit()

    def test_registration_user_wrong_password_impossible(self, driver):
        driver.get(configuration.MAIN_PAGE + configuration.REG_PAGE)
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.REG_BUTTON))
        driver.find_element(*TestLocators.REG_NAME).send_keys(data.new_user_wrong_password['name'])
        driver.find_element(*TestLocators.REG_E_MAIL).send_keys(data.new_user_wrong_password['e-mail'])
        driver.find_element(*TestLocators.REG_PASSWORD).send_keys(data.new_user_wrong_password['password'])
        driver.find_element(*TestLocators.REG_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(TestLocators.REG_BUTTON))
        wrong_pass = driver.find_element(*TestLocators.WRONG_PASSWORD).text
        driver.quit()
        assert wrong_pass == "Некорректный пароль"
