"""
Sometimes you'll want to spread out your classes over several modules
to keep any one file from growing too large and avoid storing 
unrelated classes in the same module. When you store your classes in 
several modules, you may find that a class in one module depends on a
class in another module. When this happens, you can import the required 
class into the first module.

For example, let's store the Car class in one module and the ElectricCar 
and Battery classes in a separate module. We'll make a new module called 
electric_car.py - replacing the electric_car.py file we created earlier-
and copy just the Battery and ElectricCar classes into this file:
(A concise version will be printed here, please refer to - 
modules/car_v2.py and modules/electric_car.py)
"""

# from car import Car

# class Battery():
#     --snip--

# class ElectricCar(Car):
#     --snip--


"""
The class ElectricCar needs access to its parent class Car, so we import Car 
directly into the module at line 17. If we forget this line, Python will raise
and error when we try to make an ElectricCar instance. We also need to update
the car_v2 module so it only contains the Car class.

Now we can import from each module separately and create whatever kind of car 
we need:
"""


# from car_v2 import Car
# from electric_car import ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())

# my_tesla = ElectricCar('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())

"""
We import Car from its module, and ElectricCar from its module. We then create
a regular car and one electric car. Both kinds of cars are created correctly.
For proof of concept, access modules/my_cars_v2.py.
"""
