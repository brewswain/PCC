"""
This chapter will cover how to use Python's dictionaries, which allow you to connect pieces
of related information. You can access, as well as modify the information once it's in a
dictionary. You can loop through dictionaries. You can also nest dictionaries inside lists, 
lists inside dictionaries, and dictionaries inside other dictionaries.
"""

# A Simple Dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])


# Working with Dictionaries

"""
A dictionary in Python is a collection of key-value pairs. Each key is connected to a value,
and you can use a key to access the value associated with a key. A key's value can be a number,
a string, a list, or even another dictionary.

A key-value pair is a set of values that are associated with each other. When you provide a key,
Python returns the value associated with it.  Every key is connected to its value by a colon, and 
individual key-value pairs are separated by commas.

The syntax for dictionaries  are as seen below:
"""

alien_0 = {'color': 'green', 'points': 5}


# Accessing Values in a Dictionary

"""
To get the value associated with a key, give the name of the dictionary and then place the key
inside a set of square brackets:
print(alien_0['color])

This returns the value associated with the key 'color', which is 'green'.

You can have an unlimited number of key-=value pairs in a dictionary.
"""

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']

print('You just earned ' + str(new_points) + ' points!')
