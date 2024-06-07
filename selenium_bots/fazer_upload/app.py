from selenium.webdriver.common.by import By
from time import sleep

from configs.web_driver import config_web_driver

SITE = 'https://cursoautomacao.netlify.app/'

driver = config_web_driver()

def acessar_site(site):
    driver.get(site)
    sleep(5)

def rolar_pagina():
    driver.execute_script("window.scrollTo(0, 2400);")
    sleep(3)

def busca_pelo_botao_de_upload():
    botao_upload = driver.find_element(By.XPATH, '//input[@type="file"]')
    return botao_upload

def seleciona_arquivo(botao):
    caminho = 'C:\\Users\\gabri\\Documents\\Projects\\TinyBots\\selenium_bots\\fazer_upload\\teste.txt'
    botao.send_keys(caminho)
    sleep(3)

def enviar_arquivo():
    botao_enviar = driver.find_element(By.XPATH, '//input[@value="Enviar Arquivo"]')
    if botao_enviar is not None:
        botao_enviar.click()
        sleep(3)
        fechar_alerta()
    else:
        print('Botão de enviar arquivo não encontrado')

def fechar_alerta():
    alerta = driver.switch_to.alert
    alerta.accept()
    sleep(3)
    print('Arquivo enviado com sucesso!')

def main():
    acessar_site(SITE)
    rolar_pagina()

    botao = busca_pelo_botao_de_upload()
    if botao is not None:
        seleciona_arquivo(botao)

    enviar_arquivo()

    input('Pressione ENTER para encerrar...')
    driver.quit()

if __name__ == '__main__':
    main()