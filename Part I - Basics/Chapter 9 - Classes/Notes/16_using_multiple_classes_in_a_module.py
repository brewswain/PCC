"""
You can store as many classes as you need in a single module, although
each class in a module should be related somehow. The classes Battery
and ElectricCar both help represent cars, so let's add them to the 
module car.py.

Now we can make a new file called my_electric_car.py, import the
ElectricCar class, and make an electric car. Please look in the 
modules folder for access to my_electric_car.py.
"""

# Importing Multiple Classes from a Module

"""
You can import as many classes as you need into a program file. If we want
to make a regular car and an electric car in the same file, we need to 
import both classes, Car and ElectricCar:
"""

# from car import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

"""
You import multiple classes from a module by separating each class with a 
comma. Once you've imported the necessary classes, you're free to make as 
many instances of each class as you need.

In this example we make a regular Volkswagen Beetle, and an electric Tesla
roadster:

===============================
|   # 2016 Volkswagen Beetle  |
|   # 2016 Tesla Roadster     |
===============================
"""
