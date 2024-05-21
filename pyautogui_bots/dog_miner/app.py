import pyautogui
import time

# Mover o mouse para a posição do botão
pyautogui.moveTo(1060, 424, duration=1)

# Clica no botão de jogar
pyautogui.click()

# Espera 15 segundos - tempo para o jogo carregar
time.sleep(15)

# Scroll para cima
pyautogui.scroll(1000)

# Mover o mouse para a posição do botão de 'START'
pyautogui.moveTo(1068, 337, duration=1)

# Clica no botão de 'START'
pyautogui.click()

# Espera 10 segundos - tempo para o jogo carregar
time.sleep(10)

# Navegar até o botão de fechar pop-up 'TO THE MOON'
pyautogui.moveTo(1218, 208, duration=1)

# Clica no botão de fechar pop-up
pyautogui.click()

# Move para a pedra de mineração
pyautogui.moveTo(996, 320, duration=1)

# Clica na pedra de mineração até quebrá-la
for i in range(30000):
    pyautogui.click()
