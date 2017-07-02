from feedgen.feed import FeedGenerator

fg = FeedGenerator()
fg.id('xxx')
fg.load_extension('podcast', atom=True)
fg.podcast.itunes_category('Technology', 'Podcasting')
fg.title('xxxx')

fe = fg.add_entry()
fe.id('http://lernfunk.de/media/654321/1/file.mp3')
fe.title('The First Episode')
fe.author({'name': 'John Doe', 'email': 'john@example.de'})
fe.link(href='http://example.com', rel='alternate')
fe.description('Enjoy our first episode.', isSummary=True)
fe.enclosure('http://lernfunk.de/media/654321/1/file.mp3', 0, 'audio/mpeg')

print(fg.atom_str(pretty=True))
