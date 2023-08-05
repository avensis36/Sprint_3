from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators


password = 'test'

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_INTO_ACCOUNT_BUTTON))
driver.find_element(*PageLocators.LOGIN_INTO_ACCOUNT_BUTTON).click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
driver.find_element(*PageLocators.REGISTER_BUTTON_ON_LOGIN).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PASSWORD_PLACEHOLDER))
driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(password)
driver.find_element(*PageLocators.NAME_INPUT).click()
assert 'Некорректный пароль' in driver.find_element(*PageLocators.INCORRECT_PASSWORD_TEXT).text

driver.quit()

