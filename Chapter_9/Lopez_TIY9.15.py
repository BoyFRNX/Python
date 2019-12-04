from random import choice

numbers_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

random_1 = choice(numbers_letters)
random_2 = choice(numbers_letters)
random_3 = choice(numbers_letters)
random_4 = choice(numbers_letters)

print(f"Anyone matching these four selections wins a prize:\
      \n-{random_1}\n-{random_2}\n-{random_3}\n-{random_4}")

my_ticket = []


def random_ticket(ticket_name):
    """Random ticket generator."""
    while ticket_name:
        ticket_name.pop(0)
    while len(my_ticket) < 4:
        ticket_name.insert(-1, choice(numbers_letters))


def ticket_checker(ticket_name):
    """Check winning conditions for the ticket."""
    number_correct = 0
    count = 0
    active = True
    while active:
        count += 1
        for ticket in my_ticket:
            if ticket == random_1:
                number_correct += 1
            elif ticket == random_2:
                number_correct += 1
            elif ticket == random_3:
                number_correct += 1
            elif ticket == random_4:
                number_correct += 1
        if number_correct == 4:
            print(f"Congrats, you won! It only took {count} loops to get a winning ticket.")
            active = False
        else:
            random_ticket(ticket_name)
            number_correct = 0


random_ticket(my_ticket)
ticket_checker(my_ticket)
