from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://nces.ed.gov/globallocator/index.asp?search=1&State=AL&city=Abbeville&zipcode=&miles=&itemname=&sortby=state&School=1&PrivSchool=1&College=1&CS=DE4547D0")
time.sleep(0.5)

distritos = Select(driver.find_element(By.XPATH, '//*[@id="state"]'))
tela_cidades = driver.find_element(By.PARTIAL_LINK_TEXT,'Browse')
todas_opcoes = distritos.options

for distrito in todas_opcoes:
    opcao_atual = distrito.get_attribute('value')
    
    if opcao_atual and opcao_atual != 'OTHER':
        distrito.click()
        time.sleep(1)
        tela_cidades.click()
        time.sleep(1)
        janela_atual = driver.window_handles
        driver.switch_to.window(janela_atual[1])
        time.sleep(1)
        nome_cideades = driver.find_elements(By.TAG_NAME, 'li')
    
        for n in nome_cideades:
            print(n.text)
        
        driver.switch_to.window(janela_atual[0])