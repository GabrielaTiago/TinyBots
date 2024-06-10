import scrapy
from typing import Any, Iterable
from scrapy.http import Response, Request

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes_to_scrape' # Identificador

    # REQUEST: Objeto que contém a URL da página da web
    # Cria uma requisição para a página da web quotes.toscrape.com
    def start_requests(self) -> Iterable[Request]:
        urls = ['http://quotes.toscrape.com']

        for url in urls:
            yield Request(url=url, callback=self.parse)

    # RESPONSE: Objeto que contém o conteúdo da página da web
    # Clona a página da web, criando um arquivo quotes.html
    def parse(self, response: Response, **kwargs: Any) -> None:
        with open('quotes.html', 'wb') as file:
            file.write(response.body)