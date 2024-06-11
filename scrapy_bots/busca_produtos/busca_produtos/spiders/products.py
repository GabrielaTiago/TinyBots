
from busca_produtos.configs.web_driver import config_web_driver
from scrapy import Spider
from scrapy.http import Request, Response
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ProductsScraperSpider(Spider):
    name = 'products'
    allowed_domains = ['dadosdinamicos.netlify.app']
    start_urls = ['https://dadosdinamicos.netlify.app/']

    def __init__(self):
        self.driver, self.wait = config_web_driver()
        self.xpath = '//table/tr[@class="pro-list-info"]'

    # Request
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse, meta={'prox_url': url})

    def parse(self, response: Response):
        self.driver.get(response.meta['prox_url'])
        res_web_driver = Selector(text=self.driver.page_source)

        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.xpath))) # aguarda carregamento das linhas da tabela

        while True:
            for product in res_web_driver.xpath(self.xpath):
                pro = product.xpath("./td[1]/text()").get()
                price = product.xpath("./td[2]/text()").get()
                rating = product.xpath("./td[3]/text()").get()

                yield {
                    'product': pro,
                    'price': price,
                    'rating': rating
                }

            try:
                next_page = self.driver.find_element(By.XPATH, '//ul/li/button[text()="Next"]')
                next_page.click()

                self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.xpath))) # aguarda carregamento das linhas da tabela
                yield Request(url=self.driver.current_url, callback=self.parse, meta={'prox_url': self.driver.current_url})
            except Exception as e:
                print(e)
                break
        self.driver.close()
