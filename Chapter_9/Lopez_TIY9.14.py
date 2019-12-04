from random import choice

numbers_letters = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

random_1 = choice(numbers_letters)
random_2 = choice(numbers_letters)
random_3 = choice(numbers_letters)
random_4 = choice(numbers_letters)

print(f"Anyone matching one of these four selections wins a prize:\
      \n-{random_1}\n-{random_2}\n-{random_3}\n-{random_4}")
