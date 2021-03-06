from comics.aggregator.crawler import GoComicsComCrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'FoxTrot'
    language = 'en'
    url = 'http://www.gocomics.com/foxtrot'
    start_date = '1988-04-10'
    rights = 'Bill Amend'

class Crawler(GoComicsComCrawlerBase):
    history_capable_date = '2006-12-27'
    schedule = 'Su'
    time_zone = -5

    def crawl(self, pub_date):
        return self.crawl_helper('FoxTrot', pub_date)
