from comics.aggregator.crawler import GoComicsComCrawlerBase
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Pearls Before Swine'
    language = 'en'
    url = 'http://www.gocomics.com/pearlsbeforeswine/'
    start_date = '2001-12-30'
    rights = 'Stephan Pastis'

class Crawler(GoComicsComCrawlerBase):
    history_capable_date = '2002-01-06'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5

    def crawl(self, pub_date):
        return self.crawl_helper('Pearls Before Swine', pub_date)
