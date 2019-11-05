cities = {
    'Chicago': {
        'country': 'United States',
        'population': '2.75 Million',
        'fact': 'Nickname is the Windy City'
    },
    'New York': {
        'country': 'United States',
        'population': '20.04 Million',
        'fact': 'Nickname is the Big Apple'
    },
    'Indianapolis': {
        'country': 'United States',
        'population': '869,012',
        'fact': 'Nickname is Crossroads of America'
    },
}

for city, info in cities.items():
    print(f"{city.title()}:\n")
    for key, value in info.items():
        print(f"\t{key.title()}: {value.title()}")
    print("\n")
