favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }

take_poll = ['hayden', 'james', 'edward', 'jackson']

for person in take_poll:
    if person in favorite_languages:
        print(f"{person.title()}, thank you for your response!\n")
    else:
        print(f"{person.title()}, we invite you to take the Favorite Languages poll!\n")
