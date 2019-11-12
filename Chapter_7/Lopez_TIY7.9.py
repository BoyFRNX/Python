sandwich_orders = ['slim 1', 'pastrami', 'slim 3', 'pastrami', 'pastrami']

finished_sandwiches = []

print("We have run out of pastrami!")
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
    print(f"I made your {finished_sandwich.title()}.")

print("All sandwiches are finished.")
