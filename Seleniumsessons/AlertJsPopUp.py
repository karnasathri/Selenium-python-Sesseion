import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi?mobilelogin=1")

driver.find_element(By.NAME, 'proceed').click()
time.sleep(3)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
#alert.dismiss()

driver.switch_to.default_content()

