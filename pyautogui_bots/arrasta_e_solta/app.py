import pyautogui

QTD_ARQUIVOS_NA_PASTA = 9

for i in range(QTD_ARQUIVOS_NA_PASTA):
    # Move o mouse para a pasta principal
    pyautogui.moveTo(948, 210, duration=1)
    # Arrasta o arquivo para a pasta secundária
    pyautogui.dragTo(948, 620, duration=1, button='left')
