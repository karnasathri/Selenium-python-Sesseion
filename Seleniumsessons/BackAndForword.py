from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.find_element(By.LINK_TEXT, 'Best Sellers').click()

driver.back()
driver.forward()
driver.back()
driver.refresh()