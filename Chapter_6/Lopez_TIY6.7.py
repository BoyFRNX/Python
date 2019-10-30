people = {
    'Hayden': {
        'first_name': 'Hayden',
        'last_name': 'Heche',
        'age': '18',
        'city': 'Fort Wayne'
    },
    'Aung': {
        'first_name': 'Aung',
        'last_name': 'Han',
        'age': '17',
        'city': 'Fort Wayne'
    },
    'Jackson': {
        'first_name': 'Jackson',
        'last_name': 'Foote',
        'age': '17',
        'city': 'Fort Wayne'
    },
    'Tristan': {
        'first_name': 'Tristan',
        'last_name': 'Taylor',
        'age': '17',
        'city': 'Garrett'
    },
    'Tarron': {
        'first_name': 'Tarron',
        'last_name': 'White',
        'age': '16',
        'city': 'Fort Wayne'
    }
}

for person, person_info in people.items():
    print(f"{person.title()}\n")
    for key, value in person_info.items():
        print(f"\t{key.title()}: {value.title()}\n")
