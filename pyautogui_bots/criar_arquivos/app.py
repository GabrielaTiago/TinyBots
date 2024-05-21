import pyautogui

QTD_ARQUIVOS_CRIADOS = 10

for i in range(QTD_ARQUIVOS_CRIADOS):
    # Move o mouse para a pasta e clica com o botão esquerdo
    pyautogui.rightClick(1122, 265, duration=0.5);
    # Move o mouse para a opção 'Novo'
    pyautogui.leftClick(1050, 420, duration=0.5);
    # Move o mouse e clica na opção 'Arquivo txt'
    pyautogui.leftClick(1150, 550, duration=0.5);
    # Limpar o campo default do arquivo
    pyautogui.press('backspace')
    # Digitar o nome do arquivo
    pyautogui.write(f'arquivo{i+1}.txt', interval=0.1)
    # Pressionar a tecla Enter para criar o arquivo
    pyautogui.press('enter')