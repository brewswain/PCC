"""
Now we need a method to check whether an alien is at either edge, and we need to modify
update() to allow each alien to move in the appropriate direction:
"""

# alien.py


def check_edges(self):
    """Return True if alien is at edge of screen."""
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right:
        return True
    elif self.rect.left <= 0:
        return True


def update(self):
    """Move the alien right or left."""
    self.x += (self.ai_settings.alien_speed_factor *
               self.ai_settings.fleet_direction)
    sef.rect.x = self.x


"""
We can call the new method check_edges() on any alien to see if it's at the left or right
edge. The alien is at the right edge is the right attribute of its rect is greater than or
equal to the right attribute of the screen's rect(line 12). It's at the left edge if its 
left value is less than or equal to 0(line 14). 

We modify the method update() to alllow motion to the left or right(line 20) by multiplying
the alien's speed factor by the value of fleet_direction. If fleet_direction is 1, the value
of alien_speed_factor will be added to the alien's current position, moving the alien to 
the right; if fleet_direction is -1, the value will be subtracted from the alien's position,
moving the alien to the left.
"""
