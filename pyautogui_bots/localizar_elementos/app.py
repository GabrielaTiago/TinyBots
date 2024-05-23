import pyautogui

#  Localizar elementos na tela

botao_historico = pyautogui.locateOnScreen('botao_historico_calc.png')
botao_historico_point =  pyautogui.center(botao_historico)

px, py = botao_historico_point

pyautogui.click(px, py, duration=1, button='left')

# ---- OUTRA FORMA DE FAZER ----
# x, y = pyautogui.locateCenterOnScreen('botao_historico_calc.png')
# pyautogui.click(x, y, duration=1, button='left')
