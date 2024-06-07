from time import sleep
from selenium.webdriver.common.by import By

from configs.web_driver import config_web_driver

def pega_nome_do_usuario():
    print('Qual a sua graça?')
    nome = input('R: ')
    while nome == '':
        print('Por favor, digite seu nome.')
        nome = input('R: ')
    return nome

def acessar_site(driver):
    SITE = 'https://cursoautomacao.netlify.app/desafios'
    driver.get(SITE)
    sleep(4)

def rolar_pagina(driver):
    driver.execute_script("window.scrollTo(0, 330);")

def encontrar_formulario(driver):
    div_desafio = driver.find_element(By.CLASS_NAME, 'desafios2')
    return div_desafio

def encontrar_campo_nome(elemento_pai):
    input_nome = elemento_pai.find_element(By.ID, 'dadosusuario')
    return input_nome

def preecher_campo(driver, nome: str):
    if div_desafio := encontrar_formulario(driver):
        if campo_nome := encontrar_campo_nome(div_desafio):
            campo_nome.clear()
            campo_nome.send_keys(nome)
            sleep(3)

def selecionar_botao_clique_aqui(driver):
    botao = driver.find_element(By.ID, 'desafio2')
    if botao is not None:
        botao.click()
        sleep(3)

def preencher_campo_novo(driver, nome: str):
    input_nome = driver.find_element(By.ID, 'escondido')
    if input_nome is not None:
        input_nome.clear()
        input_nome.send_keys(nome)
        sleep(3)

def clicar_boao_validar(driver):
    botao = driver.find_element(By.ID, 'validarDesafio2')
    if botao is not None:
        botao.click()
        sleep(3)

def main():
    nome = pega_nome_do_usuario()
    driver = config_web_driver()  # Move the driver initialization here
    acessar_site(driver)
    rolar_pagina(driver)
    preecher_campo(driver, nome)
    selecionar_botao_clique_aqui(driver)
    preencher_campo_novo(driver, nome)
    clicar_boao_validar(driver)

    input('Precione Enter para encerrar...\n')
    driver.quit()

if __name__ == '__main__':
    main()