from user import User


class Privileges:
    """A class related to all admin privileges."""

    def __init__(self, *privileges):
        """Initializes privileges attribute."""
        self.privileges = privileges

    def show_privileges(self):
        """Shows all privileges an admin has."""
        print("Displaying admin privileges...")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):
    """A child class of User that is specific for admins."""

    def __init__(self, first_name, last_name, age, location, gender, *privilege_input):
        """Initializes first and last name, age, location, gender and any privileges given to admin."""
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = Privileges(*privilege_input)
