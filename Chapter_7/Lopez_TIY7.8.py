sandwich_orders = ['slim 1', 'slim 2', 'slim 3', 'slim 4', 'slim 5']

finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
    print(f"I made your {finished_sandwich.title()}.")

print("All sandwiches are finished.")
