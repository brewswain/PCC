"""
You can also import an entire module and then access the classes you need
using dot notation. This approach is simple and results in code that is
easy to read. Because every call that creates an instance of a class
includes the module name, you won't have naming conflicts with any names
used in the current file.

Here's what it looks like to import the entire car module and then create
a regular car and an electric car:
"""

#  import car

# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

"""
At line 12 we import the entire car module. We then access the classes we 
need through the module_name.class_name syntax. We again create a
Volkswagen beetle, and a Tesla roadster.
"""
