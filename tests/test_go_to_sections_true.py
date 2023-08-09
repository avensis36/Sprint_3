from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import PageLocators

class TestSections:
    def test_go_to_toppings_section(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
        driver.find_element(*PageLocators.TOPPINGS_SECTION_TAB).click()

        after_click = driver.find_element(*PageLocators.TOPPINGS_SECTION_TAB).get_attribute('class')
        assert after_click == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_go_to_sauces_section(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
        driver.find_element(*PageLocators.SAUCES_SECTION).click()

        after_click = driver.find_element(*PageLocators.SAUCES_SECTION_TAB).get_attribute('class')
        assert after_click == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

    def test_go_to_buns_section(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(PageLocators.MAKE_A_BURGER_HEADER))
        driver.find_element(*PageLocators.SAUCES_SECTION).click()
        driver.find_element(*PageLocators.BUNS_SECTION).click()

        after_click = driver.find_element(*PageLocators.BUNS_SECTION_TAB).get_attribute('class')
        assert after_click == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"



