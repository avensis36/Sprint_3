from selenium.webdriver.common.by import By


class PageLocators:
    LOGIN_INTO_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    MAKE_A_BURGER_HEADER = (
        By.XPATH, ".//h1[text()='Соберите бургер']")  # Заголовок "Соберите бургер" на странице конструктора
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    STELLAR_BURGERS_LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип Stellar Burgers
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    BUNS_SECTION = (By.XPATH, ".//span[text()='Булки']")  # Раздел "Булки"
    SAUCES_SECTION = (By.XPATH, ".//span[text()='Соусы']")  # Раздел "Соусы"
    TOPPINGS_SECTION = (By.XPATH, ".//span[text()='Начинки']")  # Раздел "Начинки"
    BUNS_SECTION_HEADER = (By.XPATH, ".//h2[text()='Булки']")  # Заголовок раздела булок
    SAUCES_SECTION_HEADER = (By.XPATH, ".//h2[text()='Соусы']")  # Заголовок раздела соусов
    TOPPINGS_SECTION_HEADER = (By.XPATH, ".//h2[text()='Начинки']")  # Заголовок раздела начинок
    BUNS_SECTION_TAB = (By.XPATH, ".//span[text()='Булки']/parent::div")  # Таб секции булок
    SAUCES_SECTION_TAB = (By.XPATH, ".//span[text()='Соусы']/parent::div")  # Таб секции соусов
    TOPPINGS_SECTION_TAB = (By.XPATH, ".//span[text()='Начинки']/parent::div")  # Таб секции начинок

    LOGIN_HEADER = (By.XPATH, ".//h2[text()='Вход']")  # Заголовок "Вход" на странице входа
    LOGIN_BUTTON_ON_LOGIN = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти" на /login
    REGISTER_BUTTON_ON_LOGIN = (By.XPATH, ".//a[@href='/register']")  # Кнопка регистрации на /login
    FORGOT_PASSWORD_BUTTON_ON_LOGIN = (By.XPATH, ".//a[@href='/forgot-password']")  # Кнопка восстановления пароля

    NAME_PLACEHOLDER = (By.XPATH, ".//label[text()='Имя']")  # Плейсхолдер имени
    PASSWORD_PLACEHOLDER = (By.XPATH, ".//label[text()='Пароль']")  # Плейсхолдер пароля
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле ввода почты
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле ввода пароля
    REGISTRATION_BUTTON_ON_REGISTER = (
    By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка регистрации на /register
    LOGIN_BUTTON_ON_REGISTER = (By.XPATH, ".//a[@href='/login']")  # Кнопка входа на /register
    INCORRECT_PASSWORD_TEXT = (
        By.XPATH, ".//p[@class='input__error text_type_main-default']")  # Сообщение о некорректном пароле

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']")  # Кнопка "Личный кабинет"
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")  # Кнопка выхода из личного кабинета

