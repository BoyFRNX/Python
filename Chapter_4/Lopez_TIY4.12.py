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
