from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase
import re

class Meta(MetaBase):
    name = 'Yehuda Moon'
    language = 'en'
    url = 'http://www.yehudamoon.com/'
    start_date = '2008-01-22'
    rights = '(c) 2010 Rick Smith'

class Crawler(CrawlerBase):
    history_capable_date = '2008-01-22'
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5
    has_rerun_releases = False

    def crawl(self, pub_date):
        page_url = 'http://www.yehudamoon.com/index.php?date=%s' % pub_date.strftime( "%Y-%m-%d" )
        page = self.parse_page( page_url )

        url = page.src( 'div[id="ss_img_div"] img' )
        title_full = page.text( 'option[value*="%s"]' % pub_date.strftime( "%Y-%m-%d" ) )
        title = re.sub( '^.*- *', '', title_full )
        return CrawlerImage(url, title=title)