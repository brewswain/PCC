"""
Let's add the ability to shoot bullets. We'll write code that fires a bullet(a small rectangle)
when the player presses the spacebar. Bullets will then travel straight up the screen until they
disappear off the top of the screen.
"""

# Adding the Bullet Settings

"""
First, update settings.py to include the values we'll need for a new Bullet class, at the end 
of the __init__() method:
"""
# settings.py


def __init__(self):
    --snip--

    # Bullet settings
    self.bullet_speed_factor = 1
    self.bullet.width = 3
    self.bullet.height = 15
    self.bullet_color = 60, 60, 60


"""
These settings create dark grey bullets with a width of 3 pixels and a height of 15 pixels. The
bullets will travel slightly slower than the ship.
"""
