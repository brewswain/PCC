"""
At this point, the ship will disappear off either edge of the screen if you hold down an arrow key
long enough. Let's correct this so the ship stops moving  when it reaches the edge of the screen.
We do this by modifying the update() method in Ship:
"""

# ship.py


def update(self):
    """Update the ship's position based on  movement flags."""
    # Update the ship's center value, not the rect.
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.center += self.ai_settings.ship_speed_factor
    if self.moving_left and self.rect.left > 0:
        self.center -= self.ai_settings.ship_speed_factor


"""
This code checks the position of the ship before changing  the value of self.center. The code
self.rect.right returns the x-coordinate value of the right edge of the ship's rect. If this value
is less than the value returned by self.screen_rect.right, the ship hasn't reached the right edge
of the screen (line 13).

The same goes for the left edge: it the value of the left side of the rect is greater than zero,
the ship hasn't reached the left edge of the screen (line 15). This ensures the ship is within these
bounds before adjusting the value of self.center.

If you run alien_invasion.py now, the ship should stop moving at either edge of the screen.
"""
