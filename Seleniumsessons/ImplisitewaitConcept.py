from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
#time out = 10
#dynamic wait
#implitewait will be applied for all the web elements
#global wait
#fiend elements
#fiend elements
#only for web elements
#non web elements:title,url,alerts

driver.get('https://app.hubspot.com/login/')

print(driver.title)
user_name = driver.find_element(By.ID, 'username')
user_name.send_keys('test@gmail.com')

driver.implicitly_wait(20)
driver.find_element(By.ID, 'password').send_keys('test@12345')

#driver.implicitly_wait(0)#nullify of imp wait



