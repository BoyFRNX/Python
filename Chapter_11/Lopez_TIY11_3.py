import unittest
import employee_class


class TestEmployee(unittest.TestCase):
    """Tests the methods of the Employee class."""

    def setUp(self):
        """Create an employee and their attributes and amount for a raise."""
        self.first_name = 'Joe'
        self.last_name = 'Smith'
        self.annual_salary = 40000

    def test_give_default_raise(self):
        """Test if a default raise works."""
        employee_class.Employee(self.first_name, self.last_name, self.annual_salary).give_raise()

    def test_give_custom_raise(self):
        """Test if a custom raise of 10000 works."""
        employee_class.Employee(self.first_name, self.last_name, self.annual_salary).give_raise(10000)


if __name__ == '__main__':
    unittest.main()
