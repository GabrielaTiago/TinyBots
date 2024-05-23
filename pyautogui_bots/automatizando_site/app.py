import pyautogui
from time import sleep
import webbrowser

### DADOS DO PROJETO

# Tamaho da tela
LARGURA, ALTURA = pyautogui.size()
PONTO_MEDIO = (LARGURA / 2, ALTURA / 2)
TAMANHO_SCROOL_VERTICAL = -2200
# Link do site a ser automatizado
LINK_SITE = 'https://cursoautomacao.netlify.app/'
# Temporizadores
TEMPO_CARREGAMENTO_PAGINA = 5
TEMPO_DIGITACAO = 0.5
TEMPO_ESPERA_ALERTA = 3

# Abre site
webbrowser.open_new(LINK_SITE)
# Espera site carregar
sleep(TEMPO_CARREGAMENTO_PAGINA)
# Move mouse para a janela
pyautogui.moveTo(PONTO_MEDIO[0] + 50, PONTO_MEDIO[1], duration=1)
# Descer a página até componente 'Exemplos Alertas'
pyautogui.hscroll(TAMANHO_SCROOL_VERTICAL)
# Recber nome do usuário via 'Alerta'
nome_usuario = pyautogui.prompt(title='Informações de pessoais', text='Digte seu nome:')
# Valida se o usuário digitou o nome
while nome_usuario == None:
    nome_usuario = pyautogui.prompt(title='Informação Necessária Para Continuar!!', text='Digte seu nome:')
# Selelcionar o campo 'Digite seu nome'
pyautogui.doubleClick(833, 444, duration=1)
# Preenche campo com o nome do usuário
pyautogui.write(nome_usuario, interval=0.3)
# Com a tecla 'Tab' selecionar o botão 'Alerta', e com a tecla 'enter' selecioná-lo
sleep(TEMPO_DIGITACAO)
pyautogui.press('tab')
sleep(TEMPO_DIGITACAO)
pyautogui.press('enter')
# Esperar alguns segundos para a leitura no alerta
sleep(TEMPO_ESPERA_ALERTA)
# Precinar 'enter' para confirmar leitura do alerta
pyautogui.press('enter')
# Sobe página para o início
pyautogui.press('home')
# Descer para secção de arquivos
pyautogui.press('pgdn', presses=6, interval=0.4)
# Realizar o click nos botões 'Fazer Download', para baixar os arquivos excel e pdf
pyautogui.click(849, 371, clicks=1, duration=1.5)
pyautogui.click(849, 488, clicks=1, duration=1.5)
# Alerta mostarndo que a automação foi finalizada
pyautogui.alert(title='Sucesso 🎉', text='Automação finalizada! ✅', button='OK')