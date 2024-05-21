import pyautogui

# Criar nova pasta na área de trabalho

"""
## Versão Com Clicks

# Obter a resolução da tela
width = pyautogui.size()[0]
height = pyautogui.size()[1]

# Obter o meio da tela
middle_x = width / 2
middle_y = height / 2

# Click no meio da tela
pyautogui.click(middle_x, middle_y, button='right', duration=1.5)

# Mover o mouse para a opção 'Novo'
pyautogui.click(middle_x + 20, middle_y - 125, duration=1.5)

# Mover o mouse para a opção 'Pasta'
pyautogui.click(middle_x + 300, middle_y - 125, duration=1.5)
"""

# Versão com Hotkeys

# Minimizar todas as janelas
pyautogui.hotkey('win', 'm')

# Comando criar nova pasta 'Ctrl + Shift + N'
pyautogui.hotkey('ctrl', 'shift', 'n')

# Limpar o campo default de nome da pasta
pyautogui.press('backspace')

# Digitar o nome da pasta
pyautogui.write('nova pasta feita com py', interval=0.2)

# Pressionar a tecla Enter para criar a pasta
pyautogui.press('enter')

