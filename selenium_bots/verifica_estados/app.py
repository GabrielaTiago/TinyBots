from selenium.webdriver.common.by import By

from configs.web_driver import config_web_driver

# Acessar site
SITE = 'https://cursoautomacao.netlify.app/'
driver = config_web_driver()
driver.get(SITE)

# Buscar o <a> com href="/desafios"
link_element = driver.find_element(By.XPATH, '//a[@href="/desafios"]')
# Se o elemento foi encontrado, clicar no link
if link_element is not None:
    link_element.click()
    # driver.execute_script('arguments[0].click()', link_element) # Clicar no link com JavaScript
else:
    print('Não foi encontrado o link com href="/desafios"')

# Buscar a <div> com ClassName "desafios1"
div_desafio = driver.find_element(By.CLASS_NAME, 'desafios1')
# Se a div for encontrada, buscar os botões
if div_desafio is not None:
    btns = div_desafio.find_elements(By.TAG_NAME, 'button')
    # Se os botões foram encontrados, imprimir o estado de cada um
    if btns is not None:
        for btn in btns:
            estado = 'Habilitado' if btn.is_enabled() else 'Desabilitado'
            print(f'Estado do {btn.text}: {estado}')
    else:
        print('Não foram encontrados botões na div com ClassName "desafios1"')
else:
    print('Não foi encontrado a div com ClassName "desafios1"')

input('Precione Enter para encerrar...\n')
