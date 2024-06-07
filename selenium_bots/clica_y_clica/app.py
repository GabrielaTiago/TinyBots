from time import sleep
from selenium.webdriver.common.by import By
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

def rolar_pagina_1():
    driver.execute_script("window.scrollTo(0, 240);")
    print ('\nRolando a página para baixo...\n')
    sleep(3)

def rolar_pagina_2():
    driver.execute_script("window.scrollTo(0, 1700);")
    print ('Rolando a página para baixo...\n')
    sleep(3)

def rolar_prox_elemento():
    driver.execute_script("window.scrollTo(0, 4000);")
    print('Rolando próximo elemento...\n')

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
    rolar_pagina_1()
    selecionar_radios()
    selecionar_checkboxs()
    selecionar_dropdown_classico()

    acessar_site(SITE2)
    rolar_pagina_2()
    selecionar_checkboxs_de_carros()
    selecionar_todos_os_checkboxs_de_motos()
    rolar_prox_elemento()
    selecionar_dropdown_paises()

    input('\nPressione ENTER para fechar o navegador...\n')
    driver.quit()

if __name__ == '__main__':
    main()