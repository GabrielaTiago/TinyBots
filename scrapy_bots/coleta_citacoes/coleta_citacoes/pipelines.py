# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3

from coleta_citacoes.items import QuoteItem
from scrapy.exceptions import DropItem


class SQLitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.connect('quotes.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS quotes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                quote TEXT,
                author TEXT,
                tags TEXT
            )
        ''')
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        if isinstance(item, QuoteItem):
            self.cursor.execute('''
                INSERT INTO quotes(quote, author, tags) VALUES(?, ?, ?)
            ''', (item['quote'], item['author'], item['tags']))
            self.connection.commit()
            return item
        else:
            raise DropItem('Item not recognized', item)