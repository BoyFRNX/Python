import json

fav_num = None
exists = False


def dump_fav_num(filename):
    """JSON dumps favorite number into a file."""
    with open(filename, 'w') as f:
        json.dump(fav_num, f)


def fav_num_input(filename):
    """Prompts user for their favorite number."""
    active = True
    while active:
        try:
            global fav_num
            fav_num = int(input("Please enter your favorite number: "))
        except ValueError:
            print("Please enter numbers only.")
        else:
            dump_fav_num(filename)
            active = False


def check_num_exists(filename):
    """Checks to see if a favorite number file has
    already been made. If not or file is empty, calls fav_num_input()."""
    global exists
    try:
        with open(filename) as f:
            contents = f.readline(1)
            if contents:
                exists = True
            else:
                fav_num_input(filename)
                exists = True
    except FileNotFoundError:
        fav_num_input(filename)
        exists = True


def read_fav_num(filename):
    """Loads favorite number JSON file and prints it
     with a message to the user. If no number is found, prompts user for number."""
    check_num_exists(filename)
    global exists
    global fav_num
    if exists:
        with open(filename) as f:
            fav_num = json.load(f)
            print(f"I know your favorite number! It's {fav_num} isn't it?")


read_fav_num('favorite_number.json')
