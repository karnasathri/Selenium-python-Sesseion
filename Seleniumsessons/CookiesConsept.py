from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")
print(driver.get_cookies())

#driver.add_cookie({"name": "karnasatri", "domain": "sivakarnasatri.com", "value": "python"})

#print(driver.get_cookies())
cookies = driver.get_cookies()
for cook in cookies:
  print(cook)
