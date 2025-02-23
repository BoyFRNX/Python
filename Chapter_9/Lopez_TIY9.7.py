class User:
    """An attempt to represent a user."""
    def __init__(self, first_name, last_name, age, location, gender):
        """Initializes the first name, last name, age, location and gender of the user. Sets login attempts to 0."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Describes everything known about the user."""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Gender: {self.gender}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Welcome {self.first_name} {self.last_name}!\nHow is life in {self.location}?")

    def increment_login_attempts(self):
        """Increments the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts to 0."""
        self.login_attempts = 0
        print("Resetting login attempts...")


class Admin(User):
    """A child class of User that is specific for admins."""

    def __init__(self, first_name, last_name, age, location, gender, *privileges):
        """Initializes first and last name, age, location, gender and any privileges given to admin."""
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = privileges

    def show_privileges(self):
        """Shows all privileges an admin has."""
        print("Displaying admin privileges...")
        for privilege in self.privileges:
            print(f"-{privilege}")


admin_1 = Admin('Manuel', 'Lopez', '18', 'Fort Wayne', 'Male', "can add post", "can delete post", "can change post")

admin_1.show_privileges()
