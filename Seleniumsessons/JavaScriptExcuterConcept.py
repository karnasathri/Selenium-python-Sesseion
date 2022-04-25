from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import  expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://app.hubspot.com/login/')

#best_sellers = driver.find_element(By.LINK_TEXT, 'Best Sellers')
#driver.execute_script("arguments[0].click();", best_sellers)

#title = driver.execute_script("return document.title")
#print(title)

#driver.execute_script("history.go(0);")
#driver.execute_script("alert('hello selenium');")
#inner_text = driver.execute_script("document.documentElement.innerText")
#print(driver.execute_script("return document.documentElement.innerText;"))


#form = driver.find_element(By.ID, 'hs-login')
#driver.execute_script("arguments[0].style.border = '3px solid red'", form)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#forgot_pwd = driver.find_element(By.LINK_TEXT, 'Forgot Password?')
#driver.execute_script("argument[0].scrollIntoView(true);", forgot_pwd)
#sports_header = driver.find_element(By.XPATH, "//h2[text()='Bestsellers in Bags, Wallets and Luggage']")
#driver.execute_script("argument[0].scrollIntoView(true);", sports_header)
#print(driver.execute_script("retuern navigator.userAgent"))
driver.execute_script("document.getElementById('username').value='naveen@gmail.com';")


