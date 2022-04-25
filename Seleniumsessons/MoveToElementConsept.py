import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://www.spicejet.com/')
time.sleep(3)
'''move to element'''


login_ele = driver.find_element(By.XPATH, '//*[@id="main-container"]/div/div[1]/div[2]/div[2]/div/div[3]')
login_ele.click()
#act_chins = ActionChains(driver)
#act_chins.move_to_element(login_ele).perform()

#login_ele = driver.find_element(By.)