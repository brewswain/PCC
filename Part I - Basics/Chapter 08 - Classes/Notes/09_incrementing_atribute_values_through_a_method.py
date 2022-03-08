"""
Sometimes you'll want to increment an attribute's value by a certain amount rather
than set an entirely new value. Say we buy a used car and put 100 miles on it
between the time we buy it and the time we register it. Here's a method that allows
us to pass this incremental amount and add that value  tp the odometer reading:
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


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


"""
The new method increment_odometer() at line 39 takes in a number of
miles, and adds this value to self.odometer_reading. At line 44 we create a used
car, my_used_car. We set its odometer to 23,500 by calling update_odometer() and
passing it 23500 at line 47. At line 50, we call increment_odometer() and pass it
100 to add the 100 miles that we drove between buying the car and registering it:


========================================
|   # 2013 Subaru Outback              |
|   # This car has 23500 miles on it.  |
|   # This car has 23600 miles on it.  |
========================================

You can easily modify this method to reject negative increments so no one uses
this function to roll back an odometer.
"""
