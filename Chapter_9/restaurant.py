class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurant."""
        print(f"{self.restaurant_name} is the name of this restaurant.")
        print(f"{self.restaurant_name} makes {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Prints a message saying the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Sets the number of people served to a given specific number."""
        self.number_served = number_served

    def increment_number_served(self, served):
        """Adds a specific amount to the existing amount of people served."""
        if served >= 0:
            self.number_served += served
        else:
            print("You can't serve negative people!")
