names = []

active = True
while active:
    name = input("Please enter your name (or enter 'q' to stop): ")
    print(f"Welcome {name.title()}! Enjoy your stay.\n")
    if name == 'q':
        print("Quitting...")
        active = False
    else:
        names.append(f"{name.title()} visited.\n")

with open('guest_book.txt', 'w') as file_object:
    for name in names:
        file_object.write(name)
