
from selenium.webdriver.common.by import By


class TestLocators:
    # кнопка "Зарегистрироваться" на странице регистрации
    REG_BUTTON = By.XPATH, ".//button[text() = 'Зарегистрироваться']"
    # поле "Имя" в форме регистрации
    REG_NAME = By.XPATH, ".//label[text() = 'Имя']/parent::div/input"
    # поле "Почты" в форме регистрации
    REG_E_MAIL = By.XPATH, ".//label[text() = 'Email']/parent::div/input"
    # поле "Поле" в форме регистрации
    REG_PASSWORD = By.NAME, "Пароль"
    # кнопка "Войти" на странице авторизации
    LOGIN_BUTTON = By.XPATH, ".//button[text() = 'Войти']"
    # надпись "Неправильный пароль" на странице регистрации
    WRONG_PASSWORD = By.XPATH, ".//p[@class='input__error text_type_main-default']"
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_ACC_BUTTON = By.XPATH, ".//button[text() = 'Войти в аккаунт']"
    # поле "Имя" в форме авторизации
    LOGIN_E_MAIL = By.XPATH, ".//input[@name='name']"
    # поле "Пароль" в форме авторизации
    LOGIN_PASSWORD = By.XPATH, ".//input[@name='Пароль']"
    # Кнопка "Оформить заказ" на главной странице
    MAKE_ORDER_BUTTON = By.XPATH, (".//button[@class='button_button__33qZ0 button_button_type_primary__"
                                   "1O7Bx button_button_size_large__G21Vg']")
    # Кнопка "Личный кабинет" в хэдере
    PROFILE_BUTTON = By.XPATH, ".//p[text() = 'Личный Кабинет']"
    # ссылка "Войти"
    ENTER_LINK = By.CLASS_NAME, 'Auth_link__1fOlj'
    # Кнопка "Восстановить" на странице восстановления пароля
    RESTORE_BUTTON = By.XPATH, './/button[text()="Восстановить"]'
    # кнопка "Сохранить" на странице смены пароля
    SAVE_BUTTON = By.XPATH, './/button[text()="Сохранить"]'
    # Кнопка "Конструктор" в хэдере
    CONSTRUCTOR_BUTTON = By.XPATH, ".//p[text()='Конструктор']/parent::a"
    # Логотип в хэдере
    LOGO_BUTTON = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']/a"
    # кнопка "Выход" в личном кабинете
    EXIT_PROFILE_BUTTON = By.XPATH, ".//button[text()='Выход']"
    # вкладка "Соусы" в конструкторе
    TAB_SOUS = By.XPATH, ".//span[text() = 'Соусы']/parent::div"
    # вкладка "Булки" в конструкторе
    TAB_BULKI = By.XPATH, ".//span[text() = 'Булки']/parent::div"
    # вкладка "Начинки" в конструкторе
    TAB_NACHINKI = By.XPATH, ".//span[text() = 'Начинки']/parent::div"
    # активированная вкладка в конструкторе
    CHOSEN_TAB = By.XPATH, ".//div[contains(@class,'current')]"
