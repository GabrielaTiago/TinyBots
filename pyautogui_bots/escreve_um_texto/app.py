import pyautogui
import pyperclip
import time

# Clica na área de trabalho com o botão direito
pyautogui.rightClick(832, 182, duration=1);

# Clica na opção 'Novo'
pyautogui.leftClick(880, 310, duration=1);

# Mover o mouse para a opção 'Arquivo de Texto'
pyautogui.leftClick(1080, 450, duration=1)

# Apaga o texto default
pyautogui.press('backspace')

# Renomea o arquivo
pyautogui.write('novo texto feito com py', interval=0.2)

# Pressiona a tecla Enter para criar o arquivo
pyautogui.press('enter')

# Abri o arquivo
pyautogui.click(832, 190, clicks=2)

# Aguarda o bloco de notas abrir
time.sleep(1.5)

# Clica no bloco de notas
pyautogui.click()

# Escreve o texto
texto = 'Texto feito de forma automatizada com Python!'
pyautogui.write(texto, interval=0.2)

# pyperclip.copy('Olá, mundo!') # pyperclip utilizado para textos com acentuação
# pyautogui.hotkey('ctrl', 'v')
