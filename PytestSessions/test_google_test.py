import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = None

def setup_module(module):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")

def teardown_module(module):
    driver.quit()

def test_google_title():
    assert driver.title == "Google"

def test_google_url():
    assert driver.current_url == "https://www.google.com/"
