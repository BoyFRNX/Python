# Revised code for 8.9


def show_messages(messages):
    """Loops through the list of messages and prints each message."""
    for message in messages:
        print(f"{message}\n")


message_list = ["Hi!", "How are you?", "I'm good, and you?", "The same!"]
show_messages(message_list)


# Revised code for 8.7


def make_album(artist, album, songs=None):
    """Takes an artist, album, and number of songs (if given), and puts them into a dictionary. Returns dictionary."""
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


# Revised code for 8.4


def make_shirt(size='large', message='I Love Python'):
    """Takes a size and message and prints a summary about the shirt using those parameter."""
    print(f"""You ordered a {size.lower()} and it says "{message}".""")


# Large Shirt, Default Message
make_shirt()
# Medium Shirt, Default Message
make_shirt(size='medium')
# Small Shirt, "WUNDERWORLD" message
make_shirt(size='small', message='WUNDERWORLD')
