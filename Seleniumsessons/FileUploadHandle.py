import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

driver.find_element(By.NAME, 'upfile').send_keys('C:\Users\SivakarnaSatri\Desktop')
driver.find_element(By.XPATH, "//input[@type='submit']").click()
