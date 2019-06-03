"""
Once you have a child class that inherits from a parent class, you can add
any new attributes and methods necessary to differentiate that child class
from the parent class.

Lets add an attribute that's specific to electric cars(for instance, a battery.)
and a method to report on this attribute. We'll store the battery size and write
a method that prints a description of the battery:
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

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class ElectricCar(Car):
    """Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.read_odometer()

"""
At line 55 we add a new attribute self.battery_size and set its initial value to,
say, 70. This attribute will be associated with all instances created from the
ElectricCar class but won't be associated with any instances of Car. We also add
a method called describe_battery() that prints information about the battery at
line 57. When we call this method, we get a description that is clearly specific
to an electric car:

=======================================
|   # 2016 Tesla Model S              |
|   # This car has a 70-kWh battery.  |
=======================================

There's no limit to how much you can specialize the ElectricCar Class. You can add
as many attributes and methods as you need to model an electric car to whatever 
degree of accuracy you need. An attribute or method that could belong to any car,
rather than one that's specific to an electric car, should be added to the Car class 
instead of the ElectricCar class. Then anyone who uses the Car class will have that
functionality available as well, and the ElectricCar class will only contain code 
for the information and behaviour specific to electric vehicles.
"""
