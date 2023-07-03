from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class States_selection:
    def __init__(self, tag_name: str, driver):
        self.tag_name = tag_name
        self.driver = driver

    def return_select_options(self):
        driver = self.driver
        select = Select(driver.find_element(By.TAG_NAME, self.tag_name))
        all_options = select.options
        for option in select.options:
            value_len = len(option.get_attribute('value'))
            if value_len != 2:
                all_options.remove(option)
        
        return all_options