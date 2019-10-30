rivers = {
    'nile': 'egypt',
    'maumee': 'united states',
    'amazon': 'brazil'
    }

for key, value in rivers.items():
    print(f'The {key.title()} River runs through {value.title()}.\n')
    print(f'\tName: {key.title()} River\n')
    print(f'\tCountry: {value.title()}\n')
