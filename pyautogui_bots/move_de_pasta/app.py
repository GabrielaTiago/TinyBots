import pyautogui

# Move o mouse para a pasta e clica com o botão esquerdo
pyautogui.click(948, 210, button='left', duration=0.5)

# Seleciona todos os arquivos
pyautogui.hotkey('ctrl', 'a')

# Recorta os arquivos selecionados
pyautogui.hotkey('ctrl', 'x')

# Move o mouse para a outra pasta e clica com o botão esquerdo
pyautogui.click(1122, 610, button='left', duration=0.5)

# Cola os arquivos recortados
pyautogui.hotkey('ctrl', 'v')