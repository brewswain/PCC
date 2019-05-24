"""
The below tests pertain to using conditional tests in various situations.
The goal is to have one True and one False result for each of the below.
"""

# Testing for equality and inequality in strings
car = 'Hello!'

print('\nI predict that this returns False:')
print(car == 'hello!')


song = 'The rain in Spain, stays mainly in the plain'

print('\nI predict that this returns True:')
print('again' not in song)


# Test using the lower function
pizza = 'Cheese'
print('\nI predict that this returns True:')
print(pizza.lower() == 'cheese')
print('\nI predict that this returns False:')
print(pizza.lower() != 'cheese')


# Numerical tests involving ==, !=, >, <, >=, <=

life = 42
arbitrary_number = 59034983473

print('\nI predict that this returns True:')
print(life > 25)

print('\nI predict that this returns False:')
print(arbitrary_number < life)

print('\nI predict that this returns True:')
print(life == 42)

print('\nI predict that this returns False:')
print(life != 42.0)

print('\nI predict that this returns True:')
print(arbitrary_number >= 1)

print('\nI predict that this returns False:')
print(arbitrary_number <= 59034983472)


# Tests using 'and'/'or'

bob = 'big bob'
age = 56

print('\nI predict that this returns True:')
if (bob == 'skinny bob') or (age == 56):
    print(True)

print('\nI predict that this returns False:')
if (bob == 'skinny bob') and (age == 56):
    print(True)
else:
    print(False)


# Test if item is in a list

authors = ['brandon', 'jim', 'eric']

print('\nI predict that this returns True:')

if 'tom' not in authors:
    print(True)

print('\nI predict that this returns False:')

if 'bob' in authors:
    print(True)
print(False)
