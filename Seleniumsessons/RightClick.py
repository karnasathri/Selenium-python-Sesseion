from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)

driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')

'''right/context'''
right_click_ele = driver.find_element(By.XPATH, "//span[text()='right click me']")
act_chains = ActionChains(driver)
act_chains.context_click(right_click_ele).perform()

right_click_options = driver.find_elements(By.CSS_SELECTOR, 'li.context-menu-icon span')
for ele in right_click_options:
    print(ele.text)
    if ele.text == 'Copy':
        ele.click()
        break

