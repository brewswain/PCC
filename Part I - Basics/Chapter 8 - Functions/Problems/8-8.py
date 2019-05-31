def make_album(artist_name, album_title):
    """Return a dictionary of album details."""
    album = {
        'artist': artist_name,
        'album': album_title,
    }

    return album


while True:
    print("Please insert Album details:")
    print("(Enter 'q' at any time to quit)")

    artist_input = input("Artist's name: ")
    if artist_input == 'q':
        break

    album_input = input("Album's title: ")
    if album_input == 'q':
        break

    album_dictionary = make_album(artist_input, album_input)
    print(album_dictionary)
