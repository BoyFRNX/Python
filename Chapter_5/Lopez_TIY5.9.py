user_names = []
if user_names:
    for user in user_names:
        if user == 'admin':
            print("Hello admin, would you like a status report?")
        elif user == 'me1234':
            print("Hello me1234, thank you for logging on again.")
        elif user == 'guest1':
            print("Hello guest, thank you for logging on.")
else:
    print("We need to find some users!")
