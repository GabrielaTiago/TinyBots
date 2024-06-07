from selenium.webdriver.common.by import By

from configs.web_driver import config_web_driver
from modules.credenciais import credenciais_de_login
from modules.temporizadores import pausa_curta

credenciais =  credenciais_de_login()

driver = config_web_driver()

def acessar_site():
    SITE = 'https://cursoautomacao.netlify.app/'
    driver.get(SITE)

def ir_para_login():
    # Buscar o <a> com href="/login"
    login_link = driver.find_element(By.XPATH, '//a[@href="/login"]')
    # Se o elemento foi encontrado, clicar no link
    if login_link is not None:
        pausa_curta()
        login_link.click()
    else:
        print('Não foi encontrado o link de login"')

def interage_com_campo_email():
    email_input = driver.find_element(By.XPATH, '//input[@name="email"]')
    if email_input is not None:
        pausa_curta()
        email_input.send_keys(credenciais[0])
    else:
        print('Não foi encontrado o campo de email')

def interage_com_campo_senha():
    senha_input = driver.find_element(By.XPATH, '//input[@name="campoSenha"]')
    if senha_input is not None:
        pausa_curta()
        senha_input.send_keys(credenciais[1])
    else:
        print('Não foi encontrado o campo de senha')

def enviar_formulario():
    botao_enviar = driver.find_element(By.XPATH, '//button[@type="submit"]')
    if botao_enviar is not None and botao_enviar.is_enabled():
        pausa_curta()
        botao_enviar.click()
    else:
        print('Não foi possível enviar')

def main():
    acessar_site()
    ir_para_login()
    interage_com_campo_email()
    interage_com_campo_senha()
    enviar_formulario()

    input('Pressione ENTER para fechar o navegador')
    driver.quit()

if __name__ == '__main__':
    main()