class Employee:
    """Contain valueable employee information including salary."""

    def __init__(self, first_name, last_name, salary=''):
        """Store an employee's attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = float(salary)

    def give_raise(self, amount=5000):
        """Give employee a raise, either $5000.00, or a custom amount."""
        self.salary += float(amount)
#         return self.salary


# brandon = Employee('brandon', 'lee', 57000.00)
# print(brandon.give_raise())

# brandon = Employee('brandon', 'lee', 57000.00)
# print(brandon.give_raise(3000))
