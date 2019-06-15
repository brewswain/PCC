"""
Now we'll create the settings that will make the fleet move down the screen and to the left when
it hits the right edge of the screen. Here's how to implement this behaviour.
"""

# settings.py

# Alien settings
self.alien_speed_factor = 1
self.fleet_drop_speed = 10
# fleet_direction of 1 represents rights; -1 represents left.
self.fleet_direction = 1

"""
The setting fleet_drop_speed controls how quickly the fleet drops down the screen each time an 
alien reaches either edge. It's helpful to separate this speed from the aliens' horizontal speed 
so you can adjust the two speeds independently.

To implement the setting fleet_direction, we could use a text value, such as 'left' or 'right', 
but we'd end up with if-elif statements testing for the fleet direction. Instead, because we have 
only two directions to deal with, let's use the values 1 and -1 and switch between them each time
the fleet changes direction. (Using numbers also makes sense because moving right involves adding 
to each alien's x-coordinate value, and moving left involves subtracting from each alien's 
x-coordinate value.)
"""
