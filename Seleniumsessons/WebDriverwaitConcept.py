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
driver.get('https://app.hubspot.com/login/')
wait = WebDriverWait(driver, 10)
#wait.until(ec.title_is('HubSpot Login'))
wait.until(ec.title_contains('HubSpot'))
print(driver.title)


wait = WebDriverWait(driver, 10)
email_id = wait.until(ec.presence_of_element_located((By.ID, 'username')))
email_id.send_keys('test@gamil.com')

driver.find_element(By.ID, 'password').send_keys('test@123')



