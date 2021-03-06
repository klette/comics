from comics.aggregator.crawler import GoComicsComCrawlerBase
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Get Fuzzy'
    language = 'en'
    url = 'http://www.gocomics.com/getfuzzy/'
    start_date = '1999-09-01'
    rights = 'Darby Conley'

class Crawler(GoComicsComCrawlerBase):
    history_capable_date = '2009-05-26'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5

    def crawl(self, pub_date):
        return self.crawl_helper('Get Fuzzy', pub_date)
