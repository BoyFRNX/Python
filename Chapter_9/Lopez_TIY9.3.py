class User:
    """An attempt to represent a user."""
    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender

    def describe_user(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}!\nHow is life in {self.location}?")


user_1 = User('Manuel', 'Lopez', '18', 'Fort Wayne', 'Male')
user_2 = User('Hayden', 'Heche', '18', 'Fort Wayne', 'Male')
user_3 = User('Isabella', 'Price', '10', 'Fort Wayne', 'Female')

user_1.greet_user()
user_1.describe_user()

user_2.greet_user()
user_2.describe_user()

user_3.greet_user()
user_3.describe_user()
