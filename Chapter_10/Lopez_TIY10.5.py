active = True
while active:
    response = input("Why do you like programming? (Enter 'q' to quit instead.): ")
    if response == 'q':
        print("Stopping...")
        active = False
    else:
        with open('programming_responses', 'a') as file_object:
            file_object.write(f"{response}\n")
