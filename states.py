from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from search_gov import driver

class States:
    def __init__(self, tag_name: str):
        self.tag_name = tag_name

    def return_select_options(self):
        select = Select(driver.find_element(By.TAG_NAME, self.tag_name))
        all_options = select.options
        for option in select.options:
            value_len = len(option.get_attribute('value'))
            if value_len != 2:
                all_options.remove(option)
        
        return all_options