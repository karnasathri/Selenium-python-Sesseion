from _multiprocessing import send

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\chromepath\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.google.co.in/")

driver.find_element(By.NAME, 'q').send_keys("Naveen Automationlabs")
optionslist = driver.find_elements(By.CSS_SELECTOR, 'ul.G43f7e li span')
print(len(optionslist))

for ele in optionslist:
    print(ele.text)
    if ele.text == 'naveen automationlabs youtube':
        ele.click()
        break



time.sleep(5)

driver.quit()
