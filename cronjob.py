import time

from plugins.youtube import YoutubePlugin
from settings import RSS_CHANNELS
from utils.rss import gen_podcast_rss


def update_rss_file():
    print('cronjob running')
    for channel in RSS_CHANNELS:
        if channel['type'] == 'youtube':
            title, entries = YoutubePlugin.parse_youtube_rss(channel['rss'])
        else:
            continue
        gen_podcast_rss(title=title, entries=entries, file_path='cache/%s.xml' % channel['name'])
    print('cronjob finished')

while True:
    update_rss_file()
    time.sleep(60 * 10)
