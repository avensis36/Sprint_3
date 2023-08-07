from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators
import data


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_INTO_ACCOUNT_BUTTON))
driver.find_element(*PageLocators.LOGIN_INTO_ACCOUNT_BUTTON).click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.LOGIN_HEADER))
driver.find_element(*PageLocators.REGISTER_BUTTON_ON_LOGIN).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_BUTTON_ON_REGISTER))
driver.find_element(*PageLocators.LOGIN_BUTTON_ON_REGISTER).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_HEADER))
driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(data.email)
driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(data.password)
driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.ORDER_BUTTON))
driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()
WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.NAME_PLACEHOLDER))
assert '/profile' in driver.current_url

driver.quit()

