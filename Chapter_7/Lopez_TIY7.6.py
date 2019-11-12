# Exercise 7-4 Conditional Test Version

prompt = "(Conditional Test) Please tell us what you want on your pizza (Enter 'quit' when done):"

print(prompt)

topping = None
while topping != 'quit':
    topping = input()
    if topping != 'quit':
        print(f"Adding {topping.lower()}...")

# Exercise 7-4 Active Variable Version

prompt = "(Active Variable Test) Please tell us what you want on your pizza (Enter 'quit' when done):"

print(prompt)

active = True
while active:
    topping = input()
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping.lower()}...")

# Exercise 7-4 Break Statement Version

prompt = "(Break Statement Test) Please tell us what you want on your pizza (Enter 'quit' when done):"

print(prompt)

while True:
    topping = input()
    if topping.lower() == 'quit':
        break
    else:
        print(f"Adding {topping.lower()}...")
