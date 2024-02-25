def make_album(artist, title, track=None):
    """Build a dictionary containing information about an album."""
    album = {'artist': artist, 'title': title}
    if track:
        album['tracks'] = track
    return album

taylor = make_album('taylor swift', '1989')
ariana = make_album('ariana grande', 'thank u, next')

# print(taylor)
# print(ariana)

while True:
    print("\nTell me about your favorite album:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    track = input("Number of tracks (optional): ")
    if track == 'q':
        break

    album = make_album(artist, title, track)
    print(album)