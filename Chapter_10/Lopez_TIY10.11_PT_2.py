import json

filename = ''


def read_fav_num():
    """Loads favorite number JSON file and prints it with a message to the user."""
    active = True
    while active:
        try:
            global filename
            filename = input("Please enter a file name: ")
            with open(filename) as f:
                fav_num = json.load(f)
        except FileNotFoundError:
            print(f"The file '{filename}' could not be found.")
        else:
            print(f"I know your favorite number! It's {fav_num} isn't it?")
            active = False


read_fav_num()
