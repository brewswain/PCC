import unittest
from employee_class import Employee


class TestEmployeeSalary(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create a test employee to use in tests."""
        self.brandon = Employee('brandon', 'lee', 57000.00)

    def test_give_default_raise(self):
        """Test that by default, a raise of $5000.00 is given."""
        self.brandon.give_raise()
        self.assertEqual(self.brandon.salary, 62000.00)

    def test_give_custom_raise(self):
        """Test that giving a custom raise works."""
        self.brandon.give_raise(3000)
        self.assertEqual(self.brandon.salary, 60000.00)


unittest.main()
