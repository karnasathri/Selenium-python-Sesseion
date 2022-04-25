import xlrd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains, DesiredCapabilities
import time

workbook = xlrd.open_workbook('C:\\Users\\SivakarnaSatri\\Desktop\Working\Data1.xlsx')

sheet = workbook.sheet_by_name('Login')

rowCount = sheet.nrows
colCount = sheet.ncols
print(rowCount)
print(colCount)

for curr_row in range(1, rowCount):
    user_name = sheet.cell_value(curr_row,0)
    password = sheet.cell_value(curr_row, 1)

    print(user_name + " " + password)
