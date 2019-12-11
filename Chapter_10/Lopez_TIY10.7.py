active = True
while active:
    first_number = input("Please enter the first number: ")
    second_number = input("Please enter the second number ")
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Please only enter numbers.")
    else:
        print(f"The sum of {first_number} and {second_number} is {result}.")
        active = False
