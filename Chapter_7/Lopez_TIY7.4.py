prompt = "Please tell us what you want on your pizza (Enter 'quit' when done):"

print(prompt)

active = True
while active:
    topping = input()
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"Adding {topping.lower()}...")
