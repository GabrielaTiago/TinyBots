from configs.crawler import championship_bot_config
from spiders.championship import ChampionshipSpider


def main():
    bot = championship_bot_config()

    bot.crawl(ChampionshipSpider)
    bot.start()

if __name__ == '__main__':
    main()