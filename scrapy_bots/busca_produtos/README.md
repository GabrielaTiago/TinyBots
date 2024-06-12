# Coleta Sitações

Bot criado para navegar em uma SPA(Single Page Aplication) e coletar informações sobre nome, preço e avaliação dos produtos listados, retornando um arquivo csv com as informações coletadas

## Rodando

1. Abra o terminal e navegue até o diretório do projeto `TinyBots`

2. Insira os comandos:

    ```bash
    cd scrapy_bots/busca_produtos
    ```

    ```bash
    scrapy crawl products -O data.csv
    ```

3. A automação irá iniciar

Observe a criação do arquivo `data.csv` no diretório `scrapy_bots/busca_produtos`
