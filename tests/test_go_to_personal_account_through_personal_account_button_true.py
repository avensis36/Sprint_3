from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PageLocators.PERSONAL_ACCOUNT_BUTTON))
driver.find_element(*PageLocators.PERSONAL_ACCOUNT_BUTTON).click()
assert driver.current_url != "https://stellarburgers.nomoreparties.site/"

driver.quit()

