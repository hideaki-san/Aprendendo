from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as ex
import time

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://en.wikipedia.org/wiki/Lists_of_schools_in_the_United_States")
time.sleep(1)
elements = driver.find_elements(By.PARTIAL_LINK_TEXT,'district')
time.sleep(1)
for element in elements:
    try:
        time.sleep(1)
        element.click()
        time.sleep(1)
        driver.back()
        time.sleep(1)
    except ex.ElementNotInteractableException:
        print("Elemento não interagivel!")
    except ex.StaleElementReferenceException:
        print("Elemento Obsoleto!")
    except ex.ElementClickInterceptedException:
        print("Click interceptado!")
