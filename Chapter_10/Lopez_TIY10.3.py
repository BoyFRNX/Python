guest_name = input("Please enter your name: ")

filename = 'guests.txt'
with open(filename, 'w') as file_object:
    file_object.write(guest_name)
