class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is the name of this restaurant.")
        print(f"{self.restaurant_name} makes {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant_1 = Restaurant('Olive Garden', 'Italian')
restaurant_2 = Restaurant("Casa's", "Italian")
restaurant_3 = Restaurant('Liberty Diner', 'Greek')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
