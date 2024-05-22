import pyautogui

# Pede informações de login ao usuário
email = pyautogui.prompt(title='Informações de login', text='Digte seu email:')
senha = pyautogui.password(title='Informações de login', text='Digte sua senha:', mask='*')

# Salva as informações de login em um arquivo
with open('login.txt', 'w') as f:
    f.write(f'Email: {email}\nSenha: {senha}')