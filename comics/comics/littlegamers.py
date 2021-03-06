from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Little Gamers'
    language = 'en'
    url = 'http://www.little-gamers.com/'
    start_date = '2000-12-01'
    rights = 'Christian Fundin & Pontus Madsen'

class Crawler(CrawlerBase):
    history_capable_date = '2000-12-01'
    schedule = 'Mo,We'
    time_zone = 1

    def crawl(self, pub_date):
        feed = self.parse_feed(
            'http://www.little-gamers.com/category/comic/feed')
        for entry in feed.for_date(pub_date):
            url = entry.summary.src('img')
            title = entry.title
            return CrawlerImage(url, title)
