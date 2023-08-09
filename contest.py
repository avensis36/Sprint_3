import pytest
from selenium.webdriver.chrome import webdriver


@pytest.fixture()
def driver():
    browser = webdriver.Chrome()
    browser.get("https://stellarburgers.nomoreparties.site/")
    yield browser
    browser.quit()