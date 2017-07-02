import re

import datetime

import pytz
import requests
from bs4 import BeautifulSoup

from settings import HTTP_HEADERS


# youku = Youku()


class YoukuPlugin(object):
    @classmethod
    def handle(cls, url):
        html = requests.get(url=url, headers=HTTP_HEADERS).text
        soup = BeautifulSoup(html, 'lxml')
        ret = []
        for s in soup.find_all('a', href=re.compile('^//v.youku.com/v_show/')):
            if s['target'] == 'video':
                # link = youku.get_video_info('http' + s['href'])
                video_data = {
                    'id': s['title'],
                    'title': s['title'],
                    'description': s['title'],
                    'published': datetime.datetime.now(tz=pytz.UTC),
                    'link': 'http:' + s['href'],
                    'type': 'video/mp4',
                }
                ret.append(video_data)
        return s['title'], ret
