import random
from selenium.webdriver.common.by import By
from time import sleep

from configs.web_driver import config_web_driver

driver = config_web_driver()

SITE1 = 'https://cursoautomacao.netlify.app/desafios'
SITE2 = 'https://cursoautomacao.netlify.app'
JANELA_INICIAL = driver.current_window_handle

def acessar_pagina(site: str):
    driver.get(site)
    sleep(3)

def rolar_pagina(inicio: int, fim: int|str):
    driver.execute_script(f'window.scrollTo({inicio}, {fim});')
    sleep(3)

def fechar_navegador():
    input('Pressione ENTER para fechar o navegador...')
    driver.quit()

def busca_botao_mudar_de_pagina():
    h5 = driver.find_element(By.XPATH, '//h5[text()="Desafios 7"]')
    pai_h5 = h5.find_element(By.XPATH, '..')
    botao = pai_h5.find_element(By.XPATH, './/button')
    return botao

def mudar_de_pagina():
    janelas = driver.window_handles
    for janela in janelas:
        if janela not in JANELA_INICIAL:
            driver.switch_to.window(janela)
            break
    sleep(2)

def clicar_botao(botao):
    botao.click()
    sleep(2)
    mudar_de_pagina()

def acessar_campo_de_texto_by_id(id: str):
    input_texto = driver.find_element(By.ID, id)
    input_texto.click()
    sleep(2)
    return input_texto

def digitar_texto(texto:str, input):
    for letra in texto:
        input.send_keys(letra)
        tempo_aleatorio = random.randint(1, 5)/30
        sleep(tempo_aleatorio)

def clicar_em_pesquisar():
    botao = driver.find_element(By.ID, 'fazer_pesquisa')
    botao.click()
    sleep(2)

def buscar_botao_mudar_de_janela():
    botao = driver.find_element(By.ID, 'opentab')
    return botao

def buscar_botao_alerta():
    botao = driver.find_element(By.ID, 'buttonalerta')
    return botao

def fechar_janela():
    sleep(2)
    driver.close()
    driver.switch_to.window(JANELA_INICIAL)

def main():
    acessar_pagina(site=SITE1)
    rolar_pagina(inicio=0, fim='document.body.scrollHeight')

    # Mudar de página
    botao_mudar_de_pagina = busca_botao_mudar_de_pagina()
    clicar_botao(botao_mudar_de_pagina)
    input_texto = acessar_campo_de_texto_by_id('opiniao_sobre_curso')
    digitar_texto('Texto de teste 1', input_texto)
    clicar_em_pesquisar()
    rolar_pagina(inicio=0, fim='document.body.scrollHeight')
    fechar_janela()
    input_desafio7 = acessar_campo_de_texto_by_id('campo_desafio7')
    digitar_texto('Texto de teste 2', input_desafio7)

    acessar_pagina(site=SITE2)
    rolar_pagina(inicio=0, fim=900)

    # Mudar de janela
    botao_mudar_de_janela = buscar_botao_mudar_de_janela()
    clicar_botao(botao_mudar_de_janela)
    input_senha = acessar_campo_de_texto_by_id('senha')
    digitar_texto('Texto de teste 2', input_senha)
    fechar_janela()
    alerta = buscar_botao_alerta()
    alerta.click()
    sleep(2)
    driver.switch_to.alert.accept()

    rolar_pagina(inicio=0, fim=3000)

    # Mudar para iframe
    iframe = driver.find_element(By.XPATH, f'//iframe[@src="{SITE1}.html"]')
    driver.switch_to.frame(iframe)
    rolar_pagina(inicio=0, fim=300)
    input_nome = acessar_campo_de_texto_by_id('dadosusuario')
    input_nome.send_keys('Nome')
    driver.switch_to.default_content() # Sair do iframe

    fechar_navegador()

if __name__ == '__main__':
    main()