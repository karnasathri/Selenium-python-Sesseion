from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")
#driver.get_screenshot_as_file('reddit_2.png');

'''full screenshot'''

#make sure that you are running in headless mode
S =lambda X: driver.execute_script('return document.body.parentNode'+X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('reddit_3.png');


