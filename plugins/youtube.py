import feedparser
from pytube import YouTube

from utils.cache import cache_get, cache_set


class YoutubePlugin(object):
    @classmethod
    def parse_youtube_rss(cls, rss_url):
        feeds = feedparser.parse(rss_url)
        title = feeds['feed']['title']
        ret = []
        for entry in feeds['entries']:
            video_id = entry['yt_videoid']
            _video = cache_get(video_id, None)
            if _video is not None:
                ret.append(_video)
                continue

            yt = YouTube("http://www.youtube.com/watch?v={vid}".format(vid=video_id))
            video = yt.get_videos()[0]
            video_data = {
                'id': video_id,
                'title': entry['title'],
                'description': entry['title'],
                'link': video.url,
                'type': 'video/{ext}'.format(ext=video.extension),
            }
            cache_set(video_id, video_data)
            ret.append(video_data)
        return title, ret
