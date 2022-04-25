from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/open-source/demo/")

def select_values(element, value):
    select = Select(element)
    select.select_by_visible_text(value)


ele_indus = driver.find_element(By.ID, 'Form_submitRequest_Industry')
ele_country = driver.find_element(By.ID, 'Form_submitRequest_Country')

select_values(ele_indus, 'Education')
select_values(ele_country, 'India')
#select = Select(ele_indus)
#select.select_by_visible_text('Education')
#select.select_by_index(4)
#select.select_by_value('health')
#print(select.is_multiple)
#select_con = Select(ele_country)
#select_con.select_by_visible_text('India')

#ele_indus = driver.find_elements(By.ID, 'Form_submitRequest_Industry')
#select = Select(ele_indus)

#select.select_by_visible_text('Education')
#select.select_by_index(4)

#select = Select(ele_indus)
#  print(ele.text)
#    if (ele.text == 'Automotive'):
#        ele.Click()
#        break
indus_options = driver.find_elements(By.XPATH, '//select[@id="Form_submitRequest_Country"]/option')
print(len(indus_options))
for ele in indus_options:
    print(ele.text)
    if ele.text == 'Trevel':
        ele.click()
        break





