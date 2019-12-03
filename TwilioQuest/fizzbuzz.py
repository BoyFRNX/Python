import sys

numbers = list(sys.argv[1:])

for number in numbers:
    if (int(number) % 3 == 0) & (int(number) % 5 == 0):
        print("fizzbuzz")
    elif int(number) % 3 == 0:
        print("fizz")
    elif int(number) % 5 == 0:
        print("buzz")
    else:
        print(int(number))
