# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst


def remove_blanck_spaces(value: str):
    return value.strip()

def remove_special_characters(value: str):
    return value.replace('\n', '').replace('“', '').replace('”', '').replace('\"', '')

def remove_comma(value: str):
    return value.replace(',', '')

class QuoteItem(scrapy.Item):
    quote = scrapy.Field(
        input_processor=MapCompose(remove_blanck_spaces, remove_special_characters),
        output_processor=TakeFirst()
    )
    author = scrapy.Field(
        input_processor=MapCompose(remove_blanck_spaces, remove_special_characters, remove_comma),
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(output_processor=Join(';') )

