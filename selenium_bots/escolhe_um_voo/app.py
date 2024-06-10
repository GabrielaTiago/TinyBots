from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from configs.web_driver import config_web_driver

driver, wait = config_web_driver()

## Acessar google flights
driver.get('https://www.google.com/flights')

# Rolando a página
driver.execute_script('window.scrollTo(0, 200)')

# Mapa de voos
mapa = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and @class="mCLexc"]')))
mapa.click()

# Sugestões de voos
sugestoes_de_voos = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//li[@class="lPyEac P0ukfb"]')))
# sugestoes_de_voo = wait.until(EC.visibility_of_any_elements_located((By.XPATH, "//li[@class='lPyEac P0ukfb']")))
sugestoes_de_voos[0].click()


input('Pressione ENTER para encerrar...\n')
driver.quit()
