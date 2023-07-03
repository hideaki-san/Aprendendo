
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from cities import City
import csv
import cities
import driver
import states
import windows

class School ():
    
 def __init__ (self):
     self.driver = driver.Driver()
    
 def set_type_of_school(school_type: str): #School class
    checkbox_public = driver.find_element(By.XPATH,'//*[@id="institutions"]/table/tbody/tr/td/table/tbody/tr[4]/td[3]/font/input')
    is_checked_public = checkbox_public.get_attribute('checked')
    checkbox_private = driver.find_element(By.XPATH,'//*[@id="institutions"]/table/tbody/tr/td/table/tbody/tr[5]/td[3]/font/input')
    is_checked_private = checkbox_private.get_attribute('checked')
    if 'public' in school_type.lower() and not 'private' in school_type.lower():
        if is_checked_private:
            checkbox_private.click()
        if not is_checked_public:
            checkbox_public.click()

    if 'private' in school_type.lower() and not 'public' in school_type.lower():
        if is_checked_public:
            checkbox_public.click()
        if not is_checked_private:
            checkbox_private.click()

    if 'public' in school_type.lower() and 'private' in school_type.lower():
        if not is_checked_public:
            checkbox_public.click()
        if not is_checked_private:
            checkbox_private.click()

 def ajust_description_line(description,type_school):
    description_line = description.text.splitlines()
    description_line[0] = description_line[0][2:]
    del description_line[3:]
    description_line[2] = description_line[2].replace(' ','')
    description_line[2] = description_line[2][:13]
    description_line.append(type_school)

    return description_line

 def set_school_description(csv_file, count): #School class
    public_schools_descriptions = driver.find_elements(By.ID,'hiddenitems_school')
    private_schools_descriptions = driver.find_elements(By.ID,'hiddenitems_privschool')
    spam_writer = csv.writer(csv_file, dialect='excel')
    for description in public_schools_descriptions:
        if description.get_attribute('align') != 'center':
            description_line = ajust_description_line(description,'Public')
            spam_writer.writerow(description_line)

    for description in private_schools_descriptions:
        if description.get_attribute('align') != 'center':
            description_line = ajust_description_line(description,'Private')
            spam_writer.writerow(description_line)
    return count


i = 0
distric = 0
options = return_select_options('select')
index = 0

class Csv():
    
 def csv():
  with open('US_schools.csv', 'w', newline='') as csv_file:
    spam_writer = csv.writer(csv_file, dialect='excel')
    spam_writer.writerow(["Name","Adress","Phone","Type"])
    for index in range(len(options)):
        options[index].click()
        open_citys_window()
        switch_window(1)
        citys = get_citys_names()
        driver.close()
        switch_window(0)
        set_type_of_school('public and private')
        for city in citys:
            set_city_name(city)
            i = set_school_description(csv_file,i)
            print(f'Número de escolas: {i}')
        distric += 1
        options = return_select_options('select')
        index += 1
