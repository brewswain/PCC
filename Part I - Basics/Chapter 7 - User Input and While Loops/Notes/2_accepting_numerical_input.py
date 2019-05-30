"""
When you use the input() function, Python interprets everything
the use enters as a string.
eg:

age = input('How old are you? ")
>>> 21
print(age)
>>> '21'


The user enters the number 21, but when we ask Python for the value
of age, it returns '21', the string representation of the numerical
value entered.

This causes errors when you try to use the input as a number:

age >= 18
>>> TypeError:unorderable types: str() >= int ()


We can resolve this issue by using the int() function, which tells
Python to treat the input as a numerical value.
"""

height = input('How tall are you, in inches? ')
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou gotta get a little taller before you can ride, sorry :(")


"""
When you use numerical input to do calculations and comparisons, be 
sure to convert the input value to a numerical representation first.
"""

# Using Modulo Operator

"""
You can easily use the modulo operator (%) to determine if a number is 
even or odd.
"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')
