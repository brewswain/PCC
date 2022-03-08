"""
You can change an attribute's value in 3 ways:

You can change the value directly though an instance.
You can set the value through a method.
You can increment the value through a method.

Let's look at each of these approaches:
"""

# Modifying an Attribute's value Directly

"""
The simplest way to modify the value of an attribute is to access the
attribute directly through an instance. Here we set the odometer reading
to 23 directly:
"""


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a nearly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


"""
Sometimes you'll want to access attributes directly like this, but other times you'll
want to write a method that updates the values for you.
"""
