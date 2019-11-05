# aliens.py
aliens = {
    'alien_0': {
        'color': 'green',
        'points': '5',
        'speed': 'slow'
    },
    'alien_1': {
        'color': 'yellow',
        'points': '10',
        'speed': 'medium'
    },
    'alien_2': {
        'color': 'red',
        'points': '15',
        'speed': 'fast'
    }
}

print("Original set of aliens: \n")
for alien, info in aliens.items():
    print(f"{alien}")
    print("\t\tInfo:")
    for key, value in info.items():
        print(f"\t{key.title()}: {value.title()}")
    print("\n")
