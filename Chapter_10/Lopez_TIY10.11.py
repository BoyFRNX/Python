import json

fav_num = None


def fav_num_input():
    """Prompts user for their favorite number."""
    active = True
    while active:
        try:
            global fav_num
            fav_num = int(input("Please enter your favorite number: "))
        except ValueError:
            print("Please enter numbers only.")
        else:
            active = False


def dump_fav_num():
    """JSON dumps favorite number into a file."""
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(fav_num, f)


fav_num_input()
dump_fav_num()
