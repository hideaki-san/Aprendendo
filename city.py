from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class City:
    def get_citys_names(self): #City class
        lists_of_citys = driver.find_elements(By.TAG_NAME,'li')
        city_names = []
        for li in lists_of_citys:
            city_names.append(li.text)
        return city_names

    def set_city_name(self,city_name): #City class
        input_city = driver.find_element(By.ID,'city') 
        input_city.clear()
        input_city.send_keys(city_name)
        input_city.send_keys(Keys.ENTER)
