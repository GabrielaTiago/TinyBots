from selenium.webdriver.common.by import By

from configs.web_driver import config_web_driver

# Acessar site
SITE = 'https://cursoautomacao.netlify.app/'
driver = config_web_driver()
driver.get(SITE)

# Buscar elemento por ID
botao = driver.find_element(By.ID, 'buttonalerta')
botoes = driver.find_elements(By.ID, 'buttonalerta')

if botao is not None:
    print('Foi encontrado o botão com ID buttonalerta')
if botoes is not None:
    for i, b in enumerate(botoes):
        print(f'Foi encontrado o botão com ID buttonalerta {i + 1} de {len(botoes)}')

# Buscar elemento por Name
radioBtns = driver.find_elements(By.NAME, 'exampleRadios')

if radioBtns is not None:
    for i, r in enumerate(radioBtns):
        print(f'Foi encontrado o boão radio com Name "exampleRadios" {i + 1} de {len(radioBtns)}')


# Buscar elemento por Classname
links_menu = driver.find_elements(By.CLASS_NAME, 'nav-link')

if links_menu is not None:
    for i, l in enumerate(links_menu):
        print(f'Foi encontrado o link com ClassName "nav-link" {i + 1} de {len(links_menu)}')


# Buscar elemento por Texto
link_home = driver.find_element(By.LINK_TEXT, 'Home')
link_desafio = driver.find_element(By.PARTIAL_LINK_TEXT, 'Des')

if link_home is not None:
    print('Foi encontrado o link com texto "Home"')
if link_desafio is not None:
    print('Foi encontrado o link com texto "Des"')

# Buscar elemento por Tag
titulos_h4 = driver.find_elements(By.TAG_NAME, 'h4')

if titulos_h4 is not None:
    for i, t in enumerate(titulos_h4):
        print(f'Foi encontrado o título h4 {i + 1} de {len(titulos_h4)}')

# Buscar elemento por XPath
botao_xpath = driver.find_element(By.XPATH, '//*[@id="buttonalerta"]')
botoes_xpath = driver.find_elements(By.XPATH, '//*[@id="buttonalerta"]')

if botao_xpath is not None:
    print('Foi encontrado o botão com XPath //*[@id="buttonalerta"]')
if botoes_xpath is not None:
    for i, b in enumerate(botoes_xpath):
        print(f'Foi encontrado o botão com XPath //*[@id="buttonalerta"] {i + 1} de {len(botoes_xpath)}')


# Buscar elemento por CSS Selector
h1_tag = driver.find_element(By.CSS_SELECTOR, 'h1')
form_check = driver.find_element(By.CSS_SELECTOR, 'input[class="form-check-input"]') # input.form-check-input

if h1_tag is not None:
    print('Foi encontrado o título h1')
if form_check is not None:
    print('Foi encontrado o input com CSS Selector input[class="form-check-input"]')

input('Pressione Enter para fechar...\n')
driver.close()
