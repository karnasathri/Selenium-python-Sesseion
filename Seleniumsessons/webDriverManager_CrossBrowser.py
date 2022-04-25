from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

from Seleniumsessons.HeadLessBrowser import options

browserName = 'chrome'
if browserName == 'chrome':
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browserName == "Firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)

else:
    print('plese pass the current browser Name:' + browserName)
    raise Exception('driver is not found')

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("naveenanimation30@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Test@12345")
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)

time.sleep(5)
driver.quit()

