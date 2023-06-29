from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import selenium.common.exceptions as ex
import time

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://en.wikipedia.org/wiki/Lists_of_schools_in_the_United_States")
time.sleep(0.5)
# driver.find_element(By.XPATH,f'//*[@id="rso"]/div[{i}]/div/div/div[1]/div/a/h3').click()
<<<<<<< HEAD
elements = driver.find_elements(By.PARTIAL_LINK_TEXT,'school_distric')
=======
elements = driver.find_elements(By.PARTIAL_LINK_TEXT,'school districts')
>>>>>>> 9c812d91250c2af33d5bd0580158287b89e94f5d
time.sleep(0.5)

for element in elements:
    try:
<<<<<<< HEAD
        with open("sites.txt", "a") as arquivo:
            arquivo.write(element.get_attribute("href") + "\n")
        element.click()
=======
        print(element.get_attribute('title') + '\n')
        #with open("escolas.txt", "a") as arquivo:
         #   arquivo.write(element.get_attribute('title') + '\n')

>>>>>>> 9c812d91250c2af33d5bd0580158287b89e94f5d
        time.sleep(3)
    except ex.ElementNotInteractableException:
        print("Elemento não interagivel!")
    except ex.StaleElementReferenceException:
        print("Elemento Obsoleto!")
    except ex.ElementClickInterceptedException:
        print("Click interceptado!")