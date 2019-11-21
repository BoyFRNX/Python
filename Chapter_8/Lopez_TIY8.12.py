def sandwich_maker(*toppings):
    print("\nYour sandwich has:")
    for topping in toppings:
        print(f"- {topping.title()}")


sandwich_maker('lettuce', 'bacon', 'ham')
sandwich_maker('cheese')
sandwich_maker('cheese', 'chicken', 'mustard', 'spinach')
