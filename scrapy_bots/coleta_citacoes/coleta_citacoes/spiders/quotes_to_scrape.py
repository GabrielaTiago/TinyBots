import scrapy
from typing import Iterable
from scrapy.http import Response, Request

class QuotesToScrapeSpider(scrapy.Spider):
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
            quote = element.xpath('.//div[@class="quoteText"]/text()').get()
            author = element.css('span.authorOrTitle::text').get() # .//span[@class="authorOrTitle"]/text()
            tags = element.xpath('.//div[@class="greyText smallText left"]/a/text()').getall()

            yield {
                'quote': quote,
                'author': author,
                'tags': tags
            }

        try:
            next_page = response.css('a.next_page::attr(href)').get()
            if next_page is not None:
                link_next_page = response.urljoin(next_page)
                yield response.follow(link_next_page, callback=self.parse)
        except Exception as e:
            self.logger.error(f'Error: {e}')
            print("End of the quotes.")