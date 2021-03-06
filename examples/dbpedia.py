import surf

store = surf.Store(reader = 'sparql_protocol',
                   endpoint = 'http://dbpedia.org/sparql',
                   default_graph = 'http://dbpedia.org')

print 'Create the session'
session = surf.Session(store, {})
session.enable_logging = False

PhilCollinsAlbums = session.get_class(surf.ns.YAGO['PhilCollinsAlbums'])

all_albums = PhilCollinsAlbums.all()

print 'Phil Collins has %d albums on dbpedia' % len(all_albums)

first_album = all_albums.first()
first_album.load()

print 'All covers'
for a in all_albums:
    if a.dbpedia_name:
        cvr = a.dbpedia_cover
        print '\tCover %s for "%s"' % (unicode(a.dbpedia_cover), unicode(a.dbpedia_name))
