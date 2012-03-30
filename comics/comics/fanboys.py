from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.core.comic_data import ComicDataBase

class ComicData(ComicDataBase):
    name = 'F@NB0Y$'
    language = 'en'
    url = 'http://fanboys-online.com/'
    start_date = '2006-04-19'
    rights = 'Scott Dewitt'

class Crawler(CrawlerBase):
    history_capable_days = 180
    time_zone = -5

    def crawl(self, pub_date):
        feed = self.parse_feed('http://fanboys-online.com/?feed=rss2')
        for entry in feed.for_date(pub_date):
            if 'Comic' not in entry.tags:
                continue
            url = entry.summary.src('img.comicthumbnail')
            if not url:
                continue
            url = url.replace('comics-rss', 'comics')
            title = entry.title
            return CrawlerImage(url, title)
