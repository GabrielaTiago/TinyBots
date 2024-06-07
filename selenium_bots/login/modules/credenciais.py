import os

CAMINHO_ARQUIVO = 'selenium_bots/login/login.txt'

def cria_arquivo_de_credenciais(email, senha):
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        arquivo.write(f'email: {email}\n')
        arquivo.write(f'senha: {senha}\n')

def pega_novas_credenciais():
    email = input('Digite o email: ')
    while email == '':
        print('Email não pode ser vazio!')
        email = input('Digite o email: ')
    senha = input('Digite a senha: ')
    while senha == '':
        print('Senha não pode ser vazia!')
        senha = input('Digite a senha: ')
    cria_arquivo_de_credenciais(email, senha)
    return [email, senha]

def busca_informacoes_no_aquivo():
    credencial  =[]
    if os.path.exists(CAMINHO_ARQUIVO):
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            for linha in arquivo:
                item = linha.split(': ')[1].split('\n')[0]
                credencial.append(item)
    else:
        print('Arquivo de credenciais não encontrado!\n')
        credencial = pega_novas_credenciais()
    return credencial

def credenciais_de_login():
    credencial = busca_informacoes_no_aquivo()
    email = credencial[0]
    senha = credencial[1]
    return email, senha
