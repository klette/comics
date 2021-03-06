from comics.aggregator.crawler import GoComicsComCrawlerBase
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Non Sequitur'
    language = 'en'
    url = 'http://www.gocomics.com/nonsequitur'
    start_date = '1992-02-16'
    rights = 'Wiley Miller'

class Crawler(GoComicsComCrawlerBase):
    history_capable_date = '1992-02-16'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5

    def crawl(self, pub_date):
        return self.crawl_helper('Non Sequitur', pub_date)
