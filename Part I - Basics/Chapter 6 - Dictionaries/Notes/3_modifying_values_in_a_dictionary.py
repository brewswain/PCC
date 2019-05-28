"""
To modify a value in a dictionary, give the name of the dictionary with the key in square brackets
and then the new value you want associated with that key. For example, consider an alien that
changes from green to yellow as a game progresses:
"""

alien_0 = {'color': 'green'}
print('The alien is ' + alien_0['color'] + '.')

alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'] + '.')


"""
For another, more in-depth example, let's track the position of an alien that can move at different speeds. 
"""

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x-position: ' + str(alien_0['x_position']))


# Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))

"""
We start by defining an alien with an initial x position and y position, and a speed of 'medium.
We also print the original value of x_position to see how far the alien moves to the right.

The if-elif-else chain determines how far the alien should move to the right and stores this value
in the variable 'x_increment'. If the alien's speed is 'slow', it moves one unit to the right, etc.

Once the increment has been calculated, it's added to the value of 'x_position' and the result is 
stored in the dictionary's 'x_position'.
"""
