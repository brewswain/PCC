"""
If you've tried firing at the aliens in the game's current state, you may have noticed that the
bullets have slowed down a bit. This is because Pygame is now doing more work on each pass 
through the loop. We can increase the speed of the bullets by adjusting the value of
bullet_speed_factor in settings.py. If we increase this value( to 3, for example), the bullets
should travel up the screen at a reasonable speed again:
"""

# settings.py

# Bullet settings
self.bullet_speed_factor = 3
self.bullet_width = 3
self.bullet_height = 15
self.bullet_color = 60, 60, 60
self.bullets_allowed = 5

"""
The best value for this setting depends on the speed of your system, so find a value that works
for you.
"""
