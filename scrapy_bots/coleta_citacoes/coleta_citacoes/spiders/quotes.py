import scrapy
from coleta_citacoes.items import QuoteItem
from scrapy.http import Response
from scrapy.loader import ItemLoader


class QuotesScraperSpider(scrapy.Spider):
    name = 'quotes' #  Identifies the Spider
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes']

    def parse(self, response: Response):
        """
        Parse the response and extract information from the HTML elements.

        Args:
            response (Response): The response object containing the HTML content.

        Yields:
            dict: A dictionary containing the extracted information from each element.
        """
        for element in response.xpath('//div[@class="quoteDetails"]'):
            loader = ItemLoader(item=QuoteItem(), selector=element, response=response)

            loader.add_xpath('quote', './/div[@class="quoteText"]/text()')
            loader.add_css('author', 'span.authorOrTitle::text') # .//span[@class="authorOrTitle"]/text()
            loader.add_xpath('tags', './/div[@class="greyText smallText left"]/a/text()')

            yield loader.load_item()

        try:
            next_page = response.css('a.next_page::attr(href)').get()
            if next_page is not None:
                link_next_page = response.urljoin(next_page)
                yield response.follow(link_next_page, callback=self.parse)
        except Exception as e:
            self.logger.error(f'Error: {e}')
            print("End of the quotes.")