import time

from plugins.youku import YoukuPlugin
from plugins.youtube import YoutubePlugin
from settings import RSS_CHANNELS
from utils.rss import gen_podcast_rss


def update_rss_file():
    print('cronjob running')
    for channel in RSS_CHANNELS:
        try:
            if channel['type'] == 'youtube':
                title, entries = YoutubePlugin.handle(channel['url'])
            elif channel['type'] == 'youku':
                title, entries = YoukuPlugin.handle(channel['url'])
            else:
                continue
        except Exception as e:
            print(e)
            continue
        gen_podcast_rss(title=title, entries=entries, file_path='cache/%s.xml' % channel['name'])
    print('cronjob finished')


while True:
    update_rss_file()
    time.sleep(60 * 10)
