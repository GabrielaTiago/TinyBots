<!-- Ícone do projeto -->
<p align="center"><img src="assets/robot-emoji.png" alt="emoji de um robô" height="80px"/></p>

<!-- Nome do Projeto -->
# <p align="center">TinyBots</p>

## :clipboard: Descrição

Este projeto é uma coleção de pequenos bots desenvolvidos para realizar tarefas específicas. Cada bot é projetado para executar uma determinada função e pode ser facilmente integrado em outros projetos. Sinta-se à vontade para explorar e modificar os bots de acordo com suas necessidades!

## :card_file_box: Lista dos Bots

Aqui estão os bots atualmente disponíveis neste projeto:

Baseados em PyAutoGUI:

1. [Abrir Site](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/abrir_site) — Recebe o link de um site e reliza a naveção
2. [Dog Miner](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/dog_miner) — Inicializa o jogo DogMiner, quebrando as pedras até passar de fase
3. [Nova Pasta](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/nova_pasta) — Cria uma nova pasta na área de trabalho
4. [Cria Arquivos](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/criar_arquivos) — Cria mútilplos arquivos de texto
5. [Arrasta e Solta](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/arrasta_e_solta) — Arrasta arquivos de um lugar e os solta em outro
6. [Move de Pasta](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/move_de_pasta) — Move arquivos entre pastas
7. [Escreve um Texto](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/escreve_um_texto) — Escreve um determinado texto em um arquivo
8. [Informações de Login](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/informacoes_de_login) — Coleta as informações de login do usuário
9. [Tirar Prints](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/tirar_prints) — Tira prints da tela inteira ou de uma região específica
10. [Localizar Elementos](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/localizar_elementos) — Localiza elementos na tela baseando-se na imagem provida
11. [Desabilitar Captcha](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/desabilitar_captcha) — Desabilita o captcha de um determinado site
12. [Automatizar Site](https://github.com/GabrielaTiago/TinyBots/tree/main/pyautogui_bots/automatizando_site) — Automatiza processos de um deterimnado site

Baseados em Selenium:

13. [Abrir Site](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/abrir_site) — Recebe o link de um site e reliza a navegação
2. [Localizar Elementos](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/localizar_elementos) — Localiza elementos na tela baseando-se no HTML da página
3. [Verifica Estados](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/verifica_estados) — Verifica o estado de elementos na tela
4. [Rolar Pagina](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/rolar_pagina) — Rola a página aaté o final depois até o topo
5. [Login](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/login) — Realiza o login em um site, com usuário e senha do arquivo .txt
6. [Preencher Campos](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/preencher_campos) — Preenche campos do formulário
7. [Clica Y Clica](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/clica_y_clica) — Clica em diversos tipos de elementos na tela (checkbox, radio, dropdown, etc)
8. [Fazer Upload](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/fazer_upload) — Realiza o upload de arquivos
9. [Salvar Imagens](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/salvar_imagens) — Salva as imagens de um site
10. [Pra Lá e Pra Cá](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/pra_la_e_pra_ca) — Navega entre as abas e janelas do navegador
11. [Escolhe um Voo](https://github.com/GabrielaTiago/TinyBots/tree/main/selenium_bots/escolhe_um_voo) — Escolhe um voo no Google Flights

## :rocket: Preparando o ambiente

Este projeto foi feito com [Python 3](https://www.python.org), portanto, certifique-se de ter a última versão estável rodando localmente. Como também o [pip](https://pypi.org/project/pip/).

:warning: Caso você utilize os seguintes sistemas operacionais `MacOS` ou `Linux`, utilize o `python3` e `pip3` nos lugares de **python** e **pip**, respectivamente, nos comandos abaixo.

1. Realize o clone deste projeto, no terminal de sua máquina, utilize o [git](https://git-scm.com/) e insira o seguinte comando:

    ```bash
    git clone git@github.com:GabrielaTiago/TinyBots.git
    ```

2. Entre na pasta do projeto, usando o coamndo `cd`:

    ```bash
    cd /caminho/para/TinyBots
    ```

3. Crie um ambiente virtual, de acordo com seu sistema operacional:

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - MacOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Instale as dependências necessárias

    ```bash
    pip install -r requirements.txt
    ```

:grey_exclamation: *Instruções individualizadas estão disponíveis nas pastas de cada bot*

$~$

## :bug: Possíveis problemas

Se você encontrar algum problema ao executar algum bot, tente as seguintes etapas de solução de problemas:

1. Certifique-se de ter uma conexão estável com a Internet.
2. Verifique se o URL do site está correto e acessível.
3. Verifique se você tem a versão mais recente do Python instalada.
4. Se não conseguir executar o bot, tente executá-lo com privilégios de administrador.

## :muscle: Contribuição

As contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhoria, abra uma *issue* ou envie um *pull request*.

## :woman_technologist: Autora

Gabriela Tiago de Araújo

-   email: <gabrielatiagodearaujo@outlook.com>
-   linkedin: <https://www.linkedin.com/in/gabrielatiago/>
-   portfolio: <https://gabrielatiago.vercel.app>

## :copyright: Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

$~$

[🔝 De volta ao topo](#tinybots)
