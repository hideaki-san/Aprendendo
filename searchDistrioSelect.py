from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import csv

driver = webdriver.Chrome()
driver.implicitly_wait(0.5)
driver.get("https://nces.ed.gov/globallocator/index.asp?search=1&State=AL&city=Abbeville&zipcode=&miles=&itemname=&sortby=state&School=1&PrivSchool=1&College=1&CS=DE4547D0")
time.sleep(0.5)

#lista dos distritos
distritos = Select(driver.find_element(By.XPATH, '//*[@id="state"]'))

#tela do link referente as cidades
tela_cidades = driver.find_element(By.PARTIAL_LINK_TEXT,'Browse')

#vetor com as opcao de distritos
todas_opcoes = distritos.options

#retira a marcaçao de faculdades
driver.find_element(By.XPATH, '//*[@id="institutions"]/table/tbody/tr/td/table/tbody/tr[6]/td[3]/font/input').click()

for distrito in todas_opcoes:
    #seleciona distrito atual do laço
    opcao_atual = distrito.get_attribute('value')
    
    if opcao_atual and opcao_atual != 'OTHER':
        #seleciona o distrito
        distrito.click()
        time.sleep(0.5)

        #seleciona o link com as cidades
        tela_cidades.click()
        time.sleep(0.5)
        janela_atual = driver.window_handles

        #faz a troca de tela para a variavel driver(tela atual)
        driver.switch_to.window(janela_atual[1])
        time.sleep(0.5)

        #recebe as cidades que estao no link
        cideades = driver.find_elements(By.TAG_NAME, 'li')
        nome_cidades = []
        nome_escolas = []
    
        #armazena em um vetor os nomes em formato de texto
        for n in cideades:
            nome_cidades.append(n.text)

        #volta para a tela inicial de busca
        driver.switch_to.window(janela_atual[0])

        #cria o arquivo csv
        with open('./Dados_das_escolas.csv', 'w') as arq:
            inserir_dados = csv.writer(arq, delimiter=',')

            for c in nome_cidades:
                #recebe o local onde realiza as buscas
                entrada_cidade = driver.find_element(By.ID, 'city')
                
                #limpa a entrada e insere o nome da cidade pela posiçao do vetor
                entrada_cidade.clear()
                entrada_cidade.send_keys(c)
                time.sleep(0.5)
                
                #clica no botao de busca do site
                driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[4]/input').click()
                time.sleep(0.5)
                
                #recebe uma variavel com o numero de resultados encontrados
                resultados = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]/input')
                resultado_atual = resultados.get_attribute('value')
                
                #caso tenha algum resultado
                if resultado_atual != '0':
                    #tipo da escola publica/privada
                    tipo = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div/form/div[1]") 
                
                    #listagem das escolas publicas que apareceram
                    escolas = driver.find_element(By.ID, 'hiddenitems_school')
                    nome_escolas = escolas.find_elements(By.TAG_NAME, 'a')
                    
                    #inserçao dos dados no arquivo csv
                    for n in range(len(nome_escolas)):
                        enderecos = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div/form/span[1]/table[1]/tbody/tr[{n+1}]/td[2]")
                        inserir_dados.writerow([c, 'Publica', nome_escolas[n].text, enderecos.text])
                
                    #condicional para caso haja escolas privadas na cidade
                    if len(nome_escolas) < int(resultado_atual):
                
                        #listagem das escolas privadas
                        escolas = driver.find_element(By.ID, 'hiddenitems_privschool')
                        nome_escolas = escolas.find_elements(By.TAG_NAME, 'a')
                
                        #inserção dos dados no arquivo csv
                        for n in range(len(nome_escolas)):
                            enderecos = driver.find_element(By.XPATH, f"/html/body/div[1]/div[3]/div/div/form/span[2]/table/tbody/tr[{n+1}]/td[2]")
                            inserir_dados.writerow([c, 'Privado', nome_escolas[n].text, enderecos.text])