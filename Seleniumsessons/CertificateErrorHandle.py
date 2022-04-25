from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import  expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, DesiredCapabilities
import time


#Chrome
#options = Options()
#options.add_argument('--allow-running-insecure-content')
#options.add_argument('--ignore-certificate-errors')

#desired_capabilities = DesiredCapabilities().CHROME.copy()
#desired_capabilities['acceptInsecureCerts'] = True

#options = Options()
#options.set_capability('acceptInsecureCerts', True)

#driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#driver.implicitly_wait(10)

#firefox
#profile = webdriver.FirefoxProfile()
#profile.accept_untrusted_certs = True

desired_capabilities = DesiredCapabilities().FIREFOX.copy()
desired_capabilities['acceptInsecureCerts'] = True
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), capabilities=desired_capabilities)
driver.get('https://expired.badssl.com/')
print(driver.find_element(By.TAG_NAME, 'h1').text)