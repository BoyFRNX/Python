import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    active = True
    while active:
        if username is not None:
            global username_answer
            username_answer = input(f"Is your name {username}? (Please respond with 'Y' or 'N')")
            break
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
            exit()
    active = True
    while active:
        if username_answer.upper() == 'Y':
            print(f"Welcome back, {username}!")
            break
        elif username_answer.upper() == 'N':
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
            break
        elif username_answer.upper() != 'Y' or 'N':
            print("Please only respond with 'Y' or 'N'.")


greet_user()
