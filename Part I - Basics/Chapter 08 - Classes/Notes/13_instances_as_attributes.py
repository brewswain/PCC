"""
When modeling something from the real world in code, you may find that
you're adding more and more detail to a class. You'll find that you
have a growing list of attributes and methods and that your files
are becoming lengthy. In these situations, you might recognize that
part of one class can be written as a separate class. You can break your
large class into smaller classes that can work together.

For example, if we keep adding detail to the ElectricCar class, we might
notice that we're adding many attributes and methods specific to the
car's battery. When we see this happening, we can stop and move those
attributes and methods to a separate class called Battery. Then, we can
use a Battery instance as an attribute in the ElectricCar class:
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


# class Battery():
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size

#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")


# class ElectricCar(Car):
#     """Initialize attributes of the parent class.
#     Then initialize attributes specific to an electric car.
#     """

#     def __init__(self, make, model, year):
#         """Initialise attributes of the parent class."""
#         super().__init__(make, model, year)
#         self.battery = Battery()


# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

"""
At line 52 we define a new class called Battery that doesn't inherit from any
other class. The __init__() method has one parameter, battery_size, in
addition to self. This is an optional parameter that sets the battery's size
to 70 if no value is provided. The method describe_battery() has been moved to
this class as well.

In the ElectricCar class, we now add an attribute called self.battery at
line 71. This line tells Python to create a new instance of Battery(With a
default size of 70, since we're not  specifying a value) and store that instance
in the attribute self.battery. This will happen everytime the __init__() method
is called; any ElectricCar instance will now have a Battery instance created
automatically.

We create an electric car and store it in the variable my_tesla. When we want to
describe the battery, we need to work through the car's battery attribute:

============================================
|   # my_tesla.battery.describe_battery()  |
============================================

This line tells Python to look at the instance my_tesla, find its battery attribute,
and call the method describe_battery() that's associated with the Battery instance
stored in the attribute. The output is identical to what we saw previously:

=======================================
|   # 2016 Tesla Model S              |
|   # This car has a 70-kWh battery.  |
=======================================

This looks like a lot of extra work, but now we can describe the battery in as much
detail as we want without cluttering the ElectricCar class:
"""


class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This can can go approximately " + str(range)
        message += " miles on a  full charge."
        print(message)


class ElectricCar(Car):
    """Initialize attributes of the parent class.
    Then initialize attributes specific to an electric car.
    """

    def __init__(self, make, model, year):
        """Initialise attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery()


print('\n')
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


"""
The new method get_range() at line 123 performs some simple analysis. If the battery's
capacity is 70 kWh, get_range() sets the range to 240 miles, and if the capacity is
85 kWh, it sets the range to 270 miles. It then reports this value. When we want to
use this method, we again have to call it through the car's battery attribute at
line 149.

The output tells us the range of the car based on its battery size:

===================================================================
|   # 2016 Tesla Model S                                          |
|   # This car has a 70-kWh battery.                              |
|   # This can can go approximately 240 miles on a  full charge.  |
===================================================================
"""
