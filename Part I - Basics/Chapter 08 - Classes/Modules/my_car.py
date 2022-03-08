from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


"""
The import statement at line 1 tells Python to open the car module and import
the class Car. Now we can use the Car class as if it were defined in this file. 
The output is the same as we saw earlier:


=====================================
|   # 2016 Audi A4                  |
|   # This car has 23 miles on it.  |
=====================================

"""
