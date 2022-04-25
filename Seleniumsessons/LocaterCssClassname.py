from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
#driver.find_element(By.CSS_SELECTOR, '#username').send_keys("karna9177@gmail.com")
#driver.find_element(By.CLASS_NAME, 'login-email').send_keys("karna9177@gmail.com")
#driver.find_element(By.CLASS_NAME, 'login-password').send_keys("Test@12345")
#driver.find_element(By.CLASS_NAME, 'login-submit').click()

#driver.find_element(By.CSS_SELECTOR, 'input.form-control.private-form__control.login-email').send_keys("Test@12345")
#driver.find_element(By.XPATH, "//input[@class='form-control private-form__control login-email']").send_keys("Test@9177")
#driver.find_element(By.CLASS_NAME, 'form-control private-form__cont
# rol login-email').send_keys("Test@34567")
#driver.find_element(By.LINK_TEXT, 'Sign up').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign').click()

#form-control private-form__control login-email
#form-control private-form__control login-password m-bottom-3
