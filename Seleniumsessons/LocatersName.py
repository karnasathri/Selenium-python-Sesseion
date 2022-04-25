from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(4)
driver.get("https://classic.crmpro.com/index.html")

print(driver.title)
username = driver.find_element(By.NAME, 'username')
possword = driver.find_element(By.NAME, 'password')
Login_button = driver.find_element(By.XPATH, "//input[@value='Login']")

username.send_keys("bacthautomation")
possword.send_keys("Test@12345")
Login_button.click()