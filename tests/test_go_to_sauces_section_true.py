from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators


driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
driver.find_element(*PageLocators.SAUCES_SECTION).click()

after_click = driver.find_element(*PageLocators.SAUCES_SECTION_TAB).get_attribute('class')
assert after_click == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

driver.quit()

