from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import  expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://mail.rediff.com/cgi-bin/login.cgi')

driver.find_element(By.NAME, 'proceed').click()

wait = WebDriverWait(driver, 10)
alert = wait.until(ec.alert_is_present())
print(alert.text)
alert.accept()
#driver.close()