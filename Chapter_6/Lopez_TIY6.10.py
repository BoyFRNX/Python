favorite_num = {
    'Hayden': ['12', '7'],
    'Tristan': ['36', '7'],
    'Jackson': ['22', '7'],
    'Nick': ['33', '7'],
    'Manuel': ['25', '7']
    }
for key, value in favorite_num.items():
    print(f"{key}: ")
    for num in value:
        print(num)
