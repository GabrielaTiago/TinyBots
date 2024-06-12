from scrapy.crawler import CrawlerProcess


def championship_bot_config():
    config = CrawlerProcess(
        settings={
            'FEEDS': {
                'championship.json': {
                    'format': 'json',
                    'encoding': 'utf8',
                    'store_empty': False,
                    'indent': 2,
                    'item_export_kwargs': {
                        'export_empty_fields': True,
                    },
                },
                'chasmpionship.csv': {
                    'format': 'csv',
                    'encoding': 'utf8',
                    'store_empty': False,
                    'fields_to_export': None,
                    'export_empty_fields': True,
                }
            },
        }
    )
    return config