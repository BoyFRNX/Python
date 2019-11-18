def make_album(artist, album, songs=None):
    if songs:
        album_info = {'artist': artist.title(), 'album': album.title(), 'songs': songs}
    else:
        album_info = {'artist': artist.title(), 'album': album.title()}
    return album_info


album_1 = make_album('Kanye West', 'Late Registration')
album_2 = make_album('Drake', 'Views', 20)
album_3 = make_album('LiSA', 'Catch The Moment')
album_4 = make_album('Boyfranxx', 'Until Next Time')

print(album_1)
print(album_2)
print(album_3)
print(album_4)
