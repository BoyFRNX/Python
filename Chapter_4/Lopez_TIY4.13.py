buffet_foods = ('chicken', 'rice', 'noodles', 'steak', 'salad')
print("Buffet menu:\n")
for buffet_food in buffet_foods:
    print(f"{buffet_food.title()}\n")
# buffet_foods[0] = 'egg' causes error
buffet_foods = ('chicken', 'rice', 'mac & cheese', 'ham', 'salad')
print("Buffet changed menu:\n")
for buffet_food in buffet_foods:
    print(f"{buffet_food.title()}\n")
