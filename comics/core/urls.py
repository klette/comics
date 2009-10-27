from django.conf.urls.defaults import *

from comics.core import views

YEAR = r'(?P<year>(19|20)\d{2})'
MONTH = r'(?P<month>\d{1,2})'
DAY = r'(?P<day>\d{1,2})'
DAYS = r'\+(?P<days>\d+)'
COMIC = r'(?P<comic>[0-9a-z-_]+)'

urlpatterns = patterns('',
    # View top comics
    url(r'^$', views.top_latest, name='top-latest'),
    url(r'^%s/$' % (DAYS,), views.top_show, name='top-last-days'),
    url(r'^%s/$' % (YEAR,), views.top_year, name='top-year'),
    url(r'^%s/%s/$' % (YEAR, MONTH), views.top_show, name='top-month'),
    url(r'^%s/%s/%s/$' % (YEAR, MONTH, DAY), views.top_show, name='top-date'),
    url(r'^%s/%s/%s/%s/$' % (YEAR, MONTH, DAY, DAYS),
        views.top_show, name='top-date-days'),

    # View one specific comic
    url(r'^c/$',
        views.comic_list, name='comic-list'),
    url(r'^c/%s/$' % (COMIC,),
        views.comic_latest, name='comic-latest'),
    url(r'^c/%s/%s/$' % (COMIC, DAYS),
        views.comic_show, name='comic-last-days'),
    url(r'^c/%s/%s/$' % (COMIC, YEAR),
        views.comic_year, name='comic-year'),
    url(r'^c/%s/%s/%s/$' % (COMIC, YEAR, MONTH),
        views.comic_show, name='comic-month'),
    url(r'^c/%s/%s/%s/%s/$' % (COMIC, YEAR, MONTH, DAY),
        views.comic_show, name='comic-date'),
    url(r'^c/%s/%s/%s/%s/%s/$' % (COMIC, YEAR, MONTH, DAY, DAYS),
        views.comic_show, name='comic-date-days'),

    # About page
    url(r'^about/$', views.about, name='about'),

    # We do not like robots
    url(r'^robots.txt$', views.robots, name='robots'),
)
