import scrapy
from typing import Iterable
from scrapy.http import Response, Request

class QuotesToScrapeSpider(scrapy.Spider):
    name = 'quotes' #  Identifies the Spider

    def start_requests(self) -> Iterable[Request]:
        urls = ['https://www.goodreads.com/quotes']

        for url in urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response: Response):
        """
        Parse the response and extract information from the HTML elements.

        Args:
            response (Response): The response object containing the HTML content.

        Yields:
            dict: A dictionary containing the extracted information from each element.
        """
        for element in response.xpath('//div[@class="quoteDetails"]'):
            quote = element.xpath('.//div[@class="quoteText"]/text()').get()
            author = element.css('span.authorOrTitle::text').get() # .//span[@class="authorOrTitle"]/text()
            tags = element.xpath('.//div[@class="greyText smallText left"]/a/text()').getall()

            yield {
                'quote': quote,
                'author': author,
                'tags': tags
            }