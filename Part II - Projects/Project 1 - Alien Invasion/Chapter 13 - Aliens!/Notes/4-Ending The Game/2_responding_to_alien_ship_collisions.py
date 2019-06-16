"""
Now we need to figure out what happens when an alien collides with the ship. Instead of
destroying the ship instance and creating a new one, we'll count how many times the ship has
been hit by tracking statistics for the game. (Tracking statistics will also be useful for
scoring.)

Let's write a new class, GameStats, to track game statistics, and save it as game_stats.py:
"""

# game_stats,py


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships.left = self.ai_settings.ship_limit


"""
We'll make one GameStats instance for the entire time Alien Invasion is running, but we'll need
to reset some statistics each time the player starts a new game. To do this, we'll initialize
most of the statistics in the method reset_stats() instead of directly in __init__(). We'll
call this method from __init() so the statistics are set properly when the GameStats instance
is first created(line 19), but we'll also be able to call reset_stats() any time the player
starts a new game.

Right now we have only one statistic, ships_left, the value of which will change throughout
the game. The number of ships the player starts with is stored in settings.py as ship_limit:
"""

# settings.py

# Ship settings
self.ship_speed_factor = 1.5
self.ship_limit = 3

"""
We also need to make a few changes in alien_invasion.py, to create an instance of GameStats:
"""

# alien_invasion.py

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf

--snip--

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)

--snip--

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

"""
We import the new GameStats class(line 53), make a stats instance (line 68), and then add the
stats, screen, and ship arguments in the call to update_aliens(line 76). We'll use these 
arguments to track the number of ships the player has left and to build a new fleet when an 
alien hits the ship.

When an alien hits the ship, we subtract one from the number of ships left, destroy all existing 
aliens and bullets, create a new fleet, and reposition the ship in the middle of the screen.
(We'll also pause the game for a moment so the player can notice the collision and regroup 
before a new fleet appears.)

Let's put most of this code in the function ship_hit():
"""

# game_functions.py

import sys 
from time import sleep

--snip--

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to the ship being hit by alien."""
    
    # Decrement ships_left.
    stats.ships_left -= 1

    # Empty the list of aliens and bullets.
    aliens.empty()
    bullets.empty()

    # Create a new fleet and center the ship.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Pause.
    sleep(0.5)

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    --snip--

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

"""
We first import the sleep() function from the time module to pause the game (line 96). The new
function ship_hit() coordinates the response when the ship is hit by an alien. Inside 
ship_hit(), the number of ships left is reduced by 1 (line 104), after which we empty the 
groups aliens and bullets (line 107).

Next, we create a new fleet and center the ship(line 111).(We'll add the method center_ship()
to Ship momentarily.) Finally, we pause after the updates have been made to all the game
elements but before any changes have been drawn to the screen so the player can see that their
ship has been hit(line 115). The screen will freeze momentarily, and the player will see that
the alien has hit the ship. When the sleep() function ends, the code will move on to the 
update_screen() function, which will draw the new fleet to the screen.

We also update the definition of update_aliens() to include the parameters stats, screen, and 
bullets (line 117) so it can pass these values in the call to ship_hit().

Here's the new method center_ship(); add it to the end of ship.py:
"""

# ship.py

def center_ship(self):
    """Center the ship on the screen."""
    self.center = self.screen_rect_centerx

"""
To center the ship, we set the value of the ship's center attribute to match the center of the 
screen, which we get through the screen_rect attribute.
"""