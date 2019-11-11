active = True
age = None
price = None
while active:
    print("How old are you?")
    age = int(input())
    if age < 3:
        price = 0
        active = False
    elif 3 <= age <= 12:
        price = 10
        active = False
    elif age > 12:
        price = 15
        active = False
print(f"A {age}-year old pays {price} dollars.")
