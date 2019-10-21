best_albums = ['To Pimp A Butterfly', 'Illmatic', 'Reasonable Doubt']
print(f"A list of best albums: {best_albums}")
best_albums.append('My Beautiful Dark Twisted Fantasy.')
print(f"\nI added {best_albums[-1]}")
print(f"\nUpdated list: {best_albums}")
print(f"\nHere's the list in alphabetical order: {sorted(best_albums)}")
print(f"\nHere's the list in alphabetical order, but reversed: {sorted(best_albums, reverse=True)}")
print(f"\nI'll take out {best_albums.pop(2)}.")
print(f"\nUpdated list: {best_albums}")
print(f"\nI'll remove {best_albums.pop(1)} as well.")
print(f"\nUpdated list: {best_albums}")
best_albums.insert(1, 'Aquemini')
print(f"\nI'll add {best_albums[1]} after {best_albums[0]}.")
print(f"\nUpdated list: {best_albums}")
best_albums.insert(2, 'Illmatic')
print(f"\nI'll add {best_albums[2]} back in, after {best_albums[1]}.")
print(f"\nUpdated list: {best_albums}")
print(f"\nLet's check the list length: it's {len(best_albums)} albums long!")
best_albums.reverse()
print(f"\nLet's reverse this list: {best_albums}")
best_albums.sort()
print(f"\nLet's sort it in alphabetical order: {best_albums}")
del best_albums[0]
del best_albums[0]
del best_albums[0]
del best_albums[0]
print(f"\nAlright, let's delete the list entirely: {best_albums} see?")
