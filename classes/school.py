from selenium.webdriver.common.by import By
from classes.window import WindowOperations
from classes.city import CityOperations
from classes.state import StateOperations
from selenium.common.exceptions import NoSuchElementException

import csv

class SchoolOperations:
    def __init__(self,driver):
        self.driver = driver

    def set_type_of_school(self,type_school): #School class
        checkbox_public = self.driver.find_element(By.XPATH,'//*[@id="institutions"]/table/tbody/tr/td/table/tbody/tr[4]/td[3]/font/input')
        is_checked_public = checkbox_public.get_attribute('checked')

        checkbox_private = self.driver.find_element(By.XPATH,'//*[@id="institutions"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/font/input')
        is_checked_private = checkbox_private.get_attribute('checked')

        if 'public' in type_school.lower() and not 'private' in type_school.lower():
            if is_checked_private:
                checkbox_private.click()
            if not is_checked_public:
                checkbox_public.click()

        if 'private' in type_school.lower() and not 'public' in type_school.lower():
            if is_checked_public:
                checkbox_public.click()
            if not is_checked_private:
                checkbox_private.click()

        if 'public' in type_school.lower() and 'private' in type_school.lower():
            if not is_checked_public:
                checkbox_public.click()
            if not is_checked_private:
                checkbox_private.click()

    def adjust_description_line(self,csv_file,desc,type_school):
        spam_writer = csv.writer(csv_file, dialect='excel')
        description_list = desc.text.splitlines()
        begin = 0
        for index in range(len(description_list)):
            end = index+1
            if end % 3 == 0:
                description_line = description_list[begin:end]
                description_line.append(type_school)
                spam_writer.writerow(description_line)
                begin = end

    def set_school_description(self,csv_file): #School class
        public_desc = []
        private_desc = []

        try:
            public_schools_descriptions = self.driver.find_element(By.ID,'hiddenitems_school')      
            for d in public_schools_descriptions.find_elements(By.CLASS_NAME, 'InstDesc'):
                if d.get_attribute('align') != 'center':
                    public_desc.append(d)
        except NoSuchElementException:
            pass
        
        try:
            private_schools_descriptions = self.driver.find_element(By.ID,'hiddenitems_privschool') 
            for d in private_schools_descriptions.find_elements(By.CLASS_NAME,  'InstDesc'):
                if d.get_attribute('align') != 'center':
                    private_desc.append(d)
        except NoSuchElementException:
            pass
        
        if public_desc != []:
            for description in public_desc:
                self.adjust_description_line(csv_file,description,'Public')

        if private_desc != []:
            for description in private_desc:
                self.adjust_description_line(csv_file,description,'Private')

    def search_school(self):
        window = WindowOperations(self.driver)
        city = CityOperations(self.driver)
        state = StateOperations('select',self.driver)

        self.set_type_of_school('Public Private')
        states_options = state.return_select_options()

        csv_file = open('US_schools.csv', 'w', newline='')
        spam_writer = csv.writer(csv_file, dialect='excel')
        spam_writer.writerow(["Name","Adress","Phone","Type"])

        index = 0
        result = 0
        for index in range(len(states_options)):
            states_options[index].click()
            window.open_citys_window()
            window.switch_window(1)
            citys_names = city.get_citys_names()
            self.driver.close()
            window.switch_window(0)
            for city_name in citys_names:
                city.put_city_in_input_box(city_name)
                self.set_school_description(csv_file)

            states_options = state.return_select_options()
            index += 1
        
        csv_file.close()