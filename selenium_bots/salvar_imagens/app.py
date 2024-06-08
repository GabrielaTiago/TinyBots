from time import sleep
from selenium.webdriver.common.by import By

from configs.web_driver import config_web_driver

SITE = 'https://cursoautomacao.netlify.app/'

driver = config_web_driver()

def abrir_pagina(url):
    driver.get(url)
    sleep(3)

def descer_pagina():
    driver.execute_script("window.scrollTo(0, 1500);")
    sleep(5)

def salvar_uma_imagem(alt: str):
    imagem = driver.find_element(By.XPATH, f"//img[@alt='{alt}']")
    with open('selenium_bots/salvar_imagens/imagem.jpg', 'wb') as arquivo:
        arquivo.write(imagem.screenshot_as_png)

def buscar_imagens():
    imgs = driver.find_elements(By.CLASS_NAME, 'img-thumbnail')
    if imgs is not None:
        print(f'Foram encontradas {len(imgs)} imagens')
        return imgs
    else:
        print('Não foram encontradas imagens')
        return None

def salvar_imagens(imgs):
    contador = 1
    for img in imgs:
        tirar_print(f'img_{contador}', img)
        contador += 1
    print('Imagens salvas com sucesso')

def tirar_print(name, img):
    caminho = 'selenium_bots/salvar_imagens/'

    with open(f'{caminho}/{name}.png', 'wb') as arquivo:
        arquivo.write(img.screenshot_as_png)
        sleep(1)
        print(f'Imagem {name}.png salvada')

def encerrar_navegador():
    input('Precione Enter para encerrar...\n')
    driver.quit()

def main():
    abrir_pagina(SITE)
    descer_pagina()
    imgs = buscar_imagens()
    salvar_imagens(imgs)

    encerrar_navegador()

if __name__ == '__main__':
    main()