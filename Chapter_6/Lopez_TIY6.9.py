favorite_places = {
    'Manuel': ['Chicago', 'New York'],
    'Hayden': ['Lake', 'Walmart'],
    'Tarron': ['Jefferson Point', 'Indianapolis']
    }
for name, places in favorite_places.items():
    print(f"{name}:\n")
    for place in places:
        print(place)
    print("\n")
