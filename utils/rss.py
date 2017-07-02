from feedgen.feed import FeedGenerator


def gen_podcast_rss(title, entries, file_path=None):
    """
    entry = {
        'id',
        'title',
        'description',
        'link',
        'type',
    }
    """
    fg = FeedGenerator()
    fg.load_extension('podcast', atom=True, rss=True)
    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.id(title)
    fg.title(title)
    fg.link({'href': 'https://joway.io', 'rel': 'self'})
    fg.description(title)
    for entry in entries:
        fe = fg.add_entry()
        fe.id(entry['id'])
        fe.title(entry['title'])
        fe.description(entry['description'], isSummary=True)
        fe.enclosure(entry['link'], 0, entry['type'])
        fe.link(href=entry['link'], rel='alternate')
    if file_path:
        fg.rss_file(filename=file_path)
    return str(fg.rss_str(pretty=True).decode('utf-8'))
