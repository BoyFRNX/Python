#***************4.11 REVIEWED*******************
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

#***************4.12 REVIEWED*****************
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print("My favorite foods are: \n")
for my_food in my_foods:
    print(f"{my_food}\n")

print("\nMy friends's favorite foods are: \n")
for friends_food in friends_foods:
    print(f"{friends_food}\n")

#***************4.13 REVIEWED*****************
buffet_foods = ('chicken', 'rice', 'noodles', 'steak', 'salad')

print("Buffet menu:\n")
for buffet_food in buffet_foods:
    print(f"{buffet_food.title()}\n")

# buffet_foods[0] = 'egg' causes error

buffet_foods = ('chicken', 'rice', 'mac & cheese', 'ham', 'salad')

print("Buffet changed menu:\n")
for buffet_food in buffet_foods:
    print(f"{buffet_food.title()}\n")
