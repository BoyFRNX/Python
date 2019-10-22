pizzas = ['pepperoni', 'sausage', 'meat lovers']
for pizza in pizzas:
    print(f"I love {pizza} pizza!\n")
print("I love all types of pizza!\n")
friends_pizzas = pizzas[:]
pizzas.append("cheese")
friends_pizzas.append("bbq chicken")
print("My favorite pizzas are:\n")
for pizza in pizzas:
    print(f"\t{pizza.title()}\n")
print("My friend's favorite pizzas are:\n")
for friends_pizza in friends_pizzas:
    print(f"\t{friends_pizza.title()}\n")
