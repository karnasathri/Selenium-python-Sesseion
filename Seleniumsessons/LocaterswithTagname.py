from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.freshworks.com/")

header_element = driver.find_element(By.TAG_NAME, 'h1')
print(header_element.text)
