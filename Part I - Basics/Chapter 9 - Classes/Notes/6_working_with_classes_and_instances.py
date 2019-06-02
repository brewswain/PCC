"""
You can use classes to represent many real-world situations. Once you
write a class, you'll spend most of your time working with instances 
created from that class. One of the first tasks you'll want to do is
is modify the attributes associated with a particular instance. You 
can modify the attributes of an instance directly or write methods 
that update attributes in specific ways.
"""

# The Car Class

"""
Let's write a new class representing a car. Our class will store 
information about the kind of car we're working with, and it will
have a method that summarizes this information:
"""


# class Car:
#     """A simple attempt to represent a car."""

#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""

#         self.make = make
#         self.model = model
#         self.year = year

#     def get_descriptive_name(self):
#         """Return a nearly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

"""
To make the class more interesting, let's add an attribute that changes over time. 
We'll add an attribute that stores the car's overall mileage.
"""

# Setting a Default Value for an Attribute

"""
Every attribute in a class needs an initial value, even if that value is 0 or an
empty string. In some cases, such as when setting a default value, it makes sense
to specify this initial value in the body of the __init__() method; if you do this
for an attribute, you don't have to include a parameter for that attribute.

Let's add an attribute called odometer_reading that always starts with a value of
0. We'll also add a method read_odometer() that helps us read each car's odometer:
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
my_new_car.read_odometer()

"""
This time when Python calls the __init__() method to create a new instance, it
stores the make, mode, and year values as attributes like it did in the previous
example. Then Python creates a new attribute called odometer_reading and sets its
initial value to 0 at line 65. 

We also have a new method called read_odometer that makes it easy to read a car's
mileage. Our car starts with a mileage of 0. Not many cars are sold with exactly 0 
miles on the odometer, so we need a way to change the value of this attribute.
"""
