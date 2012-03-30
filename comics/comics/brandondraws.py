import re

from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.core.comic_data import ComicDataBase
from HTMLParser import HTMLParser

class ComicData(ComicDataBase):
    name = 'Brandon Draws'
    language = 'en'
    url = 'http://drawbrandondraw.com/'
    start_date = '2010-06-29'
    active = False
    rights = 'Brandon B, CC BY-NC-SA 3.0'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        pass # Comic no longer published
