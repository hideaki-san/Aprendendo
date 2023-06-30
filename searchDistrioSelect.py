from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import selenium.common.exceptions as ex
import time

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://nces.ed.gov/globallocator/index.asp?search=1&State=AL&city=Abbeville&zipcode=&miles=&itemname=&sortby=state&School=1&PrivSchool=1&College=1&CS=DE4547D0")
time.sleep(0.5)

element = Select(driver.find_element(By.XPATH, '//*[@id="state"]'))
option_list = element.options

for list_position in range(7):
    element.select_by_index(list_position)
    time.sleep(3)