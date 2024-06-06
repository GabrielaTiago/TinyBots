from time import sleep
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

sleep(3)

# Rolar até o fim da página
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)
# Rolar até o topo da página
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
sleep(5)

# Outra maneira de rolar a página
# Rolar X quantidade em pixels(descer)
# driver.execute_script("window.scrollTo(0, 1500);")
# sleep(5)
# Rolar X quantidade em pixels(subir)
# driver.execute_script("window.scrollTo(0, -1500);")

input('Precione Enter para encerrar...\n')
driver.quit()