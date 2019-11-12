dream_vacation = {}

active = True

while active:
    name = input("What's your name? (Enter 'quit' to exit.) ")
    if name.lower() == 'quit':
        active = False
        if dream_vacation:
            print("Printing results...")
        else:
            print("Sorry, no one submitted a response!")
    else:
        dream_vacation[name] = input("What's your dream vacation spot? ")

for name, spot in dream_vacation.items():
    print(f"{name.title()}: {spot.title()}")
