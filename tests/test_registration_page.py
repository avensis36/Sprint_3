from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import PageLocators
import data
import helpers


class TestRegistration:
    def test_registration_true(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_INTO_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.LOGIN_INTO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.REGISTER_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.NAME_PLACEHOLDER))
        driver.find_element(*PageLocators.NAME_INPUT).send_keys(data.name)
        name_input = driver.find_element(*PageLocators.NAME_INPUT).get_attribute('value')
        assert name_input != '', 'Fill in the name'

        driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(helpers.random_email())
        email_input = driver.find_element(*PageLocators.EMAIL_INPUT).get_attribute('value')
        assert helpers.is_valid_email(email_input), 'Invalid email format'

        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(helpers.random_password())
        password_input = driver.find_element(*PageLocators.PASSWORD_INPUT).get_attribute('value')
        assert len(password_input) >= 6, 'Password is too short'

        driver.find_element(*PageLocators.REGISTRATION_BUTTON_ON_REGISTER).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(email_input)
        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(password_input)
        driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.ORDER_BUTTON))
        driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.NAME_PLACEHOLDER))
        assert '/profile' in driver.current_url

    def test_registration_input_password_less_than_six_symbols_appears_incorrect_password_message(self, driver):
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_INTO_ACCOUNT_BUTTON))
        driver.find_element(*PageLocators.LOGIN_INTO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
        driver.find_element(*PageLocators.REGISTER_BUTTON_ON_LOGIN).click()

        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PASSWORD_PLACEHOLDER))
        driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(data.short_password)
        driver.find_element(*PageLocators.NAME_INPUT).click()
        assert 'Некорректный пароль' in driver.find_element(*PageLocators.INCORRECT_PASSWORD_TEXT).text
