# Coleta Sitações

Bot criado para navegar em um site e coletar informações sobre sitações, autores e tags relacionadas, retornando um arquivo csv com as informações coletadas

## Rodando

1. Abra o terminal e navegue até o diretório do projeto `TinyBots`

2. Insira os comandos:

    ```bash
    cd scrapy_bots/coleta_citacoes
    ```

    ```bash
    scrapy crawl quotes -O data.csv
    ```

3. A automação irá iniciar

Observe a criação do arquivo `data.csv` no diretório `scrapy_bots/coleta_citacoes`
