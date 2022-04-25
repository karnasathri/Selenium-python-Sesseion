from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")

LinksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(LinksList))

for ele in LinksList:
    Link_text = ele.text
    print(Link_text)
    print(ele.get_attribute('href'))

imagelist = driver.find_elements(By.TAG_NAME, 'img')
print(len(imagelist))

for ele in imagelist:
    print(ele.get_attribute('src'))


