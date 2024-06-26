from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from configs.web_driver import config_web_driver

driver = config_web_driver()

OPCAO_RADIO_BTN = 'windows 10'
OPCAO_CHECKBOX_1 = 'Acesso Nível 1'
OPCAO_CHECKBOX_3 = 'Acesso Nível 3'
OPCAO_CHECKBOX_CARRO_2 = 'Carro 2'
OPCAO_CHECKBOX_CARRO_4 = 'Carro 4'
OPCAO_CHECKBOX_CARRO_5 = 'Carro 5'

SITE1 = 'https://cursoautomacao.netlify.app/'
SITE2 = 'https://cursoautomacao.netlify.app/desafios'

checkbox_xpath = 'input[@type="checkbox"]'  # Define a constant for the XPath expression

def acessar_site(site):
    driver.get(site)
    sleep(5)

def rolar_pagina(inicio: int, fim: int|str):
    driver.execute_script(f'window.scrollTo({inicio}, {fim});')
    print ('Rolando a página para baixo...\n')
    sleep(3)

def selecionar_radios():
    print('Selecionando botões radio...')
    botoes = driver.find_elements(By.XPATH, '//input[@type="radio"]')
    if botoes is not None:
        for botao in botoes:
            selecionar_opcao_radio(botao, OPCAO_RADIO_BTN)
    else:
        print('Nenhum botão radio foi encontrado.')
    print('')

def selecionar_opcao_radio(botao, text:str):
    if botao.get_attribute('value') == text:
        if botao.is_selected():
            print(f'Botão "{text}" já está selecionado.')
            sleep(2)
        else:
            botao.click()
            print(f'Botão "{text}" foi selecionado.')
            sleep(2)
    else:
        print(f'Botão com a opção "{text}" não foi encontrado.')

def busca_div_de_checkboxs():
    h4_checkbox = driver.find_element(By.XPATH, '//h4[text()="Exemplo Checkbox"]') # h4 com o texto "Exemplo Checkbox"
    div_pai_h4 = h4_checkbox.find_element(By.XPATH, '..') # div pai do h4
    div_checkbox = div_pai_h4.find_elements(By.XPATH, 'div')
    return div_checkbox

def selecionar_opcao_checkbox(botao, label, opcao:str):
    if label.text == opcao:
        botao.click()
        print(f'Botão "{opcao}" foi selecionado.')
        sleep(2)

def selecionar_checkboxs():
    print('Selecionando botões checkbox...')
    div_checkboxs = busca_div_de_checkboxs()

    if div_checkboxs is not None:
        for div in div_checkboxs:
            # dentro da div tem: um input e um label
            botao = div.find_element(By.XPATH, checkbox_xpath)
            label = div.find_element(By.XPATH, 'label')
            if botao is not None and label is not None:
                for opcao in [OPCAO_CHECKBOX_1, OPCAO_CHECKBOX_3]:
                    selecionar_opcao_checkbox(botao, label, opcao)
            else:
                print('Nenhum botão checkbox foi encontrado.')
    else:
        print('Div de checkboxs não foi encontrada.')
    print('')

def selecionar_dropdown_classico():
    print('Selecionando opção no dropdown...')
    dropdown = Select(driver.find_element(By.ID, 'paisselect'))
    dropdown.select_by_index(0) # Seleciona a segunda opção
    dropdown.select_by_value('canada') # Seleciona a opção com o value 'argentina'
    dropdown.select_by_visible_text('Brasil') # Seleciona a opção com o texto 'Brasil'
    sleep(2)
    print('')

def clicar_no_botao_com_direito():
    print('Clicando no botão com o botão direito do mouse...')
    botao = driver.find_element(By.ID, 'botao-direito')
    if botao is not None:
        chain = ActionChains(driver)
        chain.context_click(botao).pause(1).send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ARROW_DOWN).pause(1).send_keys(Keys.ENTER).perform()
        print('Botão foi clicado com o botão direito do mouse, e a opção do dropdown foi selecionada.')
        sleep(2)
        confirmar_alerta()

def confirmar_alerta():
    print('Confirmando alerta...')
    alerta = driver.switch_to.alert
    alerta.accept()
    print('Alerta foi confirmado.')
    sleep(2)

## Códigos para site de desafios

def busca_divs_com_checkboxs(tipo:str):
    # lista de divs com a class="form-check " que tenha o primeiro filho como um innput com name = "{tipo}"
    divs = driver.find_elements(By.XPATH, f'//div[@class="form-check "]/input[@name="{tipo}"]')
    divs = [div.find_element(By.XPATH, '..') for div in divs]
    return divs

def selecionar_checkboxs_de_carros():
    print('Selecionando botões checkbox de carros...')
    div_checkboxs = busca_divs_com_checkboxs('carros')

    if div_checkboxs is not None:
        for div in div_checkboxs:
            # dentro da div tem: um input e um label
            botao = div.find_element(By.XPATH, checkbox_xpath)
            label = div.find_element(By.XPATH, 'label')
            if botao is not None and label is not None:
                for opcao in [OPCAO_CHECKBOX_CARRO_2, OPCAO_CHECKBOX_CARRO_4, OPCAO_CHECKBOX_CARRO_5]:
                    selecionar_opcao_checkbox(botao, label, opcao)
            else:
                print('Nenhum botão checkbox foi encontrado.')
    else:
        print('Nenhuma div com checkboxs de carros não foi encontrada.')
    print('')

def selecionar_todos_os_checkboxs_de_motos():
    print('Selecionando botões checkbox de motos...')
    div_checkboxs = busca_divs_com_checkboxs('motos')
    if div_checkboxs is not None:
        for div in div_checkboxs:
            botao = div.find_element(By.XPATH, checkbox_xpath)
            label = div.find_element(By.XPATH, 'label')
            if botao is not None and label is not None:
                botao.click()
                print(f'Botão "{label.text}" foi selecionado.')
                sleep(1.5)
    else:
        print('Nenhuma div com checkboxs de motos não foi encontrada.')

def selecionar_dropdown_paises():
    print('Selecionando opção no dropdown de países...')
    lista_elementos = ['Estados Unidos', 'Africa', 'Chille']
    dropdown = Select(driver.find_element(By.ID, 'paisesselect'))
    for elemento in lista_elementos:
        dropdown.select_by_visible_text(elemento)
        sleep(2)

def main():
    acessar_site(SITE1)
    rolar_pagina(inicio=0, fim=240)
    # selecionar_radios()
    # selecionar_checkboxs()
    # selecionar_dropdown_classico()

    rolar_pagina(inicio=0, fim=800)
    clicar_no_botao_com_direito()

    # acessar_site(SITE2)
    # rolar_pagina(inicio=0, fim=1700)
    # selecionar_checkboxs_de_carros()
    # selecionar_todos_os_checkboxs_de_motos()
    # rolar_pagina(inicio=0, fim=4000)
    # selecionar_dropdown_paises()

    input('\nPressione ENTER para fechar o navegador...\n')
    driver.quit()

if __name__ == '__main__':
    main()