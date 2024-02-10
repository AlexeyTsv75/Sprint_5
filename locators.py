import data
import configuration
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest


class TestLocators:
    REG_BUTTON = By.XPATH, ".//button[text() = 'Зарегистрироваться']"
    REG_NAME = By.XPATH,".//fieldset[1]/div/div/input"
    REG_E_MAIL = By.XPATH,".//fieldset[2]/div/div/input"
    REG_PASSWORD = By.NAME, "Пароль"
    LOGIN_BUTTON = By.XPATH, ".//button[text() = 'Войти']"
    WRONG_PASSWORD = By.XPATH, ".//p[@class='input__error text_type_main-default']"
    LOGIN_ACC_BUTTON = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    LOGIN_E_MAIL = By.XPATH, ".//input[@name='name']"
    LOGIN_PASSWORD = By.XPATH, ".//input[@name='Пароль']"
    MAKE_ORDER_BUTTON = By.XPATH, (".//button[@class='button_button__33qZ0 button_button_type_primary__"
                                   "1O7Bx button_button_size_large__G21Vg']")
    PROFILE_BUTTON = By.XPATH, ".//p[text() = 'Личный Кабинет']"
    ENTER_LINK = By.CLASS_NAME, 'Auth_link__1fOlj'
    RESTORE_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    SAVE_BUTTON = By.XPATH, './/button[text()="Сохранить"]'

