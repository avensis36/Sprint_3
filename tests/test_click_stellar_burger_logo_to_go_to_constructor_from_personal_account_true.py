from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators


email = 'antonermolaev12999@gmail.com'
password = 'test12999'

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.LOGIN_HEADER))
driver.find_element(*PageLocators.EMAIL_INPUT).send_keys(email)
driver.find_element(*PageLocators.PASSWORD_INPUT).send_keys(password)
driver.find_element(*PageLocators.LOGIN_BUTTON_ON_LOGIN).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.STELLAR_BURGERS_LOGO))
driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click()

WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
assert 'Соберите бургер' == driver.find_element(*PageLocators.MAKE_A_BURGER_HEADER).text

driver.quit()

