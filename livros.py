from teste import livro
from selenium import webdriver

livro1 = livro("Os Zikas", "Comedia", 204)
livro1.cadastrar(33)
livro1.cadastro_livro()

abrir = webdriver.Firefox()

abrir.get("https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/first_script/")