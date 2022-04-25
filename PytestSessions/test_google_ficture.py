import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None
@pytest.fixture(scope="module")
def init_driver():
    global driver
    print("----setup----")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

    yield
    print("----teardown----")
    driver.quit()
@pytest.mark.usefixtures("init_driver")
def test_google_title():
    assert driver.title == "Google"

@pytest.mark.usefixtures("init_driver")
def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.com/"
