"""
Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time.
To add  a new key-value pair, you would give the name of the dictionary followed by the new key in 
square brackets along with the new value.
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


# Starting with an Empty Dictionary

"""
It's sometimes convenient, or even necessary, to start with an empty dictionary and then add each
new item to it. To start filling an empty dictionary, define a dictionary with an empty set of braces
and then add each key-value pair on it's own line.

You'll usually use empty dictionaries when storing user-supplied data in a dictionary or when
you write code that generates a large number of key-value pairs.
"""

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
