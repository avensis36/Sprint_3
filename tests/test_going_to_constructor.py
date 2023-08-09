from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import PageLocators
import data

class TestGoingToConstructor:
    def test_click_stellar_burger_logo_to_go_to_constructor_from_personal_account_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.STELLAR_BURGERS_LOGO))
        driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
        assert 'Соберите бургер' == driver.find_element(*PageLocators.MAKE_A_BURGER_HEADER).text

    def test_click_constructor_button_to_go_to_constructor_from_personal_account_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.CONSTRUCTOR_BUTTON))
        driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
        assert 'Соберите бургер' == driver.find_element(*PageLocators.MAKE_A_BURGER_HEADER).text
