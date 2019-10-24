age = input()
if int(age) < 2:
    print("You're a baby!")
elif (int(age) >= 2) and (int(age) < 4):
    print("You're a toddler!")
elif (int(age) >= 4) and (int(age) < 13):
    print("You're a kid!")
elif (int(age) >= 13) and (int(age) < 20):
    print("You're a teenager!")
elif (int(age) >= 20) and (int(age) < 65):
    print("You're an adult!")
elif int(age) > 65:
    print("You're an elder!")
