from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(200)
driver.get("https://www.orangehrm.com/open-source/open-source-on-demand/")

print(driver.title)

username_url = driver.find_element(By.ID, 'Form_submitForm_subdomain')
first_name = driver.find_element(By.ID, 'Form_submitForm_FirstName')
Last_name = driver.find_element(By.NAME, 'LastName')
email = driver.find_element(By.ID, 'Form_submitForm_Email')
Platform_link = driver.find_element(By.CLASS_NAME, 'link')

username_url.send_keys("naveen automationlabs")
first_name.send_keys("Karna")
Last_name.send_keys("Satri")
email.send_keys("karnasathri05@gmail.com")
Platform_link.click()