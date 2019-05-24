
"""
Testing for equality is case sensitive in Python.
eg:
"""
car = 'Audi'
car == 'audi'  # False
"""
If case matters, this behaviour is advantageous.But if case doesn't matter, you can convert
the variable's value to lowercase before doing the comparison.
"""

car = 'Audi'
car.lower() == 'audi'  # True
"""
The lower() function doesn't change the value that was originally stored in car, so this kind of
comparison can be done without affecting the original variable.
eg:
"""
car = 'Audi'
car.lower() == 'audi'  # True
print(car)  # Audi

"""
This is particularly useful when using a conditional test to ensure that every user's username is truly unique.
"""
