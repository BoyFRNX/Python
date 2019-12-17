class Employee:
    """Simple representation of employees in a company."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initializes the first and last name attributes and the annual salary attribute."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        self.annual_salary += amount
        return self.annual_salary
