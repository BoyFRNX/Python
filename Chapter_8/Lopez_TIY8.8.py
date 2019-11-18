def make_album(artist, album, songs=None):
    if songs:
        album_info = {'artist': artist.title(), 'album': album.title(), 'songs': songs}
    else:
        album_info = {'artist': artist.title(), 'album': album.title()}
    return album_info


active = True
while active:
    prompt_artist = input("Please input an artist name (enter 'q' to quit process):")
    if prompt_artist == 'q':
        break
    prompt_album = input(f"Please input an album name from '{prompt_artist}':")
    prompt_songs = int(input(f"If you'd like, input how many songs are on {prompt_album} (Enter 0 if you do not):"))
    if prompt_songs > 0:
        user_album = make_album(prompt_artist, prompt_album, prompt_songs)
        print(f"Here's the dictionary for '{prompt_album}': {user_album}")
    else:
        user_album = make_album(prompt_artist, prompt_album)
        print(f"Here's the dictionary for '{prompt_album}': {user_album}")
    quit_prompt = input("Would you like to quit or continue? (Enter 'q' to quit or type 'c' to continue):")
    if quit_prompt == 'q':
        break
    else:
        print("\nGreat! Loading process...\n")
