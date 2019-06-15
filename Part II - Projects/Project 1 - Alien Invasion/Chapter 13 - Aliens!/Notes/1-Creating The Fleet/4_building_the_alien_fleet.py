"""
To draw a fleet, we need to figure out how many aliens can fit across the screen and how many
rows of aliens can fit down the screen. We'll first figure out the horizontal spacing between
aliens and create a row, then we'll determine the vertical spacing and create an entire fleet.

To create a row, first create an empty group called aliens in alien_invasion.py to hold all
of our aliens, and then call a function in game_functions.py to create a fleet:
"""

# alien_invasion.py

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

# Make a ship, a group of bullets, and a group of aliens.
ship = Ship(ai_settings, screen)
bullets = Group()
aliens = Group()

# Create the fleet of aliens.
gf.create_fleet(ai_settings, screen, aliens)

# Start the main loop for the game
while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

"""
Because we're no longer creating aliens directly in alien_invasion.py, we don't need to import
the Alien class into this file.

Create an empty group to hold all of the aliens in the game(line 21). Then, call the new function
create_fleet() [line 24], which we'll write shortly, and pass it the ai_settings, the screen 
object, and the empty group aliens. Next, modify the call to update_screen() to give it access
to the group of aliens(line 31).

We also need to modify update_screen():
"""

# game_functions.py


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)


"""
First, we edit the update_screen() parameters from 'alien' to 'aliens'.

When you call draw() on a group(line 57), Pygame automatically draws each element in the 
group at the position defined in its rect attribute. In this case, aliens.draw(screen) 
draws each alien in the group to the screen.
"""
