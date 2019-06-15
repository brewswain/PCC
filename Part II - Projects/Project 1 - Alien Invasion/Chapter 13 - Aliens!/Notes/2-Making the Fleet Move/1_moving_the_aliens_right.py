"""
To move the aliens, we'll use an update() method in alien.py, which we'll call for each alien in 
the group of aliens. First, add a setting to control the speed of each alien:
"""

# settings.py

# Alien settings
self.alien_speed_factor = 1

"""
Then, use this setting to implement update():
"""
# alien.py


def update(self):
    """Move the alien right."""
    self.x += self.ai_settings.alien_speed_factor
    self.rect.x = self.x


"""
Every time we update an alien's position, we move it to the right by the amount stored in
alien_speed_factor. We track the alien's exact position with the self.x attribute, which can hold 
decimal values(line 18). We then use the value of self.x to update the position of the alien's 
rect(line 19). In the main while loop, we have calls to update the ship and bullets. Now we need to 
update the position of each alien as well:
"""

# alien_invasion.py

while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_aliens(aliens)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

"""
We update the alines' positions after the bullets have been updated, because we'll soon be checking
to see whether any bullets hit any aliens.

Finally, add the new function update_aliens() at the end of the file game_functions.py:
"""

# game_functions.py


def update_aliens(aliens):
    """Update the positions of all aliens in the fleet."""
    aliens.update()


"""
We use the update() method on the aliens group, which automatically calls each alien's update() method.
When you run Alien Invasion now, you should see the fleet move right and disappear off the side of the 
screen.
"""
