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
driver.find_element(By.XPATH, '//*[@id="institutions"]/table/tbody/tr/td/table/tbody/tr[6]/td[3]/font/input').click()

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
        cideades = driver.find_elements(By.TAG_NAME, 'li')
        nome_cidades = []
        nome_escolas = []
    
        for n in cideades:
            nome_cidades.append(n.text)

        driver.switch_to.window(janela_atual[0])

        for c in nome_cidades:
            entrada_cidade = driver.find_element(By.ID, 'city')
            entrada_cidade.clear()
            entrada_cidade.send_keys(c)
            time.sleep(0.5)
            botao_busca = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[4]/input')
            botao_busca.click()
            time.sleep(0.5)
            resultados = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]/input')
            resultado_atual = resultados.get_attribute('value')
            print(c)
            if resultado_atual != '0':
                tipo = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/form/div[1]") 
                escolas = driver.find_element(By.ID, 'hiddenitems_school')
                nome_escolas = escolas.find_elements(By.TAG_NAME, 'a')
                print('Escolas Publicas')
                for n in nome_escolas:
                    print(n.text)
                
                if len(nome_escolas) < int(resultado_atual):
                    escolas= driver.find_element(By.ID, 'hiddenitems_privschool')
                    nome_escolas = escolas.find_elements(By.TAG_NAME, 'a')
                    print('Escolas Privadas')
                    for n in nome_escolas:
                        print(n.text)