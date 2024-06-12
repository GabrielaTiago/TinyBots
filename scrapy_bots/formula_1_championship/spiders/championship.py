
from configs.webdriver import config_webdriver
from models.race import Race
from scrapy import Spider
from scrapy.http import Request, Response
from scrapy.loader import ItemLoader
from scrapy.selector import Selector
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ChampionshipSpider(Spider):
    name = 'championship'
    allowed_domains = ['f1races.netlify.app']
    start_urls = ['https://f1races.netlify.app']

    def __init__(self):
        self.driver, self.wait = config_webdriver()

    # Request
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse, meta={'prox_url': url})

    def load_elements(self):
        self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="sc-bZQynM llbHfj"]')))

    def parse(self, response: Response):
        self.driver.get(response.meta['prox_url'])

        self.load_elements()

        res_web_driver = Selector(text=self.driver.page_source)

        for race in res_web_driver.xpath('//div[@class="sc-bZQynM llbHfj"]'):
            loader = ItemLoader(item=Race(), selector=race, response=response)

            loader.add_xpath('name', './div[1]/text()')
            loader.add_xpath('local', './div[2]/text()')
            loader.add_xpath('winner', './div[3]/a/text()')
            loader.add_xpath('circuit_time', './div[4]/text()')

            yield loader.load_item()

        self.driver.close()
