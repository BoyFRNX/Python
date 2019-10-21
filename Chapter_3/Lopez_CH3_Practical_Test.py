halloween_candies = []
print("Please type the number of participants below:")
participants = input()
print("Please ask participants their favorite Halloween candy and type it below:")
while len(halloween_candies) < int(participants):
    halloween_candies.append(input())
print(f"From what we gathered, the favorite types of Halloween candy are: {halloween_candies}")
