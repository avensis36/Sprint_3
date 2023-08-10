from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators
import data

class TestPersonalAccountPage:
    def test_go_to_personal_account_through_personal_account_button_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.EXIT_BUTTON))
        assert driver.find_element(*PageLocators.EXIT_BUTTON).text == 'Выход'

    def test_exit_from_account_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(data.email)
        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(data.password)
        driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.EXIT_BUTTON))
        driver.find_element(*PageLocators.EXIT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        assert 'Вход' == driver.find_element(*PageLocators.LOGIN_HEADER).text
