def make_album(artist_name, album_title, album_length=''):
    """Return a dictionary of album details."""
    album = {
        'artist': artist_name,
        'album': album_title,
    }

    if album_length:
        album['amount of tracks'] = album_length
    return album


album_details = make_album('mudvayne', 'the end of all things to come', 12)
print(album_details)

album_details = make_album('schoolboy Q', 'blank face',)
print(album_details)

album_details = make_album('chronixx', 'dread and terrible',)
print(album_details)
