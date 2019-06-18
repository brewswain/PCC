"""
Finally, let's display the number of ships the player has left, but this time, let's use a 
graphic. To do so, we'll draw ships in the upper-left corner of the screen to represent how
many ships are left, like many classic arcade games do.

First, we need to make Ship inherit from Sprite so we can create a group of ships:
"""

# ship.py

from ship import Ship
from pygame.sprite import Group
import pygame.font
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        --snip--


"""
Here we import Sprite, make sure Ship inherits from Sprite(line 15), and call super() at the
beginning of __init__() [line 19].

Next, we need to modify Scoreboard to create a group of ships we can display. Here's the import
statements and __init__():

"""

# scoreboard.py


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        --snip--
        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


"""
Because we're making a group of ships, we import the Group and Ship classes. We call 
prep_ships() after the call to prep_level().

Here's prep_ships():
"""

# scoreboard.py


def prep_ships(self):
    """Show how many ships are left."""
    self.ships = Group()
    for ship_number in range(self.stats.ships_left):
        ship = Ship(self.ai_settings, self.screen)
        ship.rect.x = 10 + ship_number * ship.rect.width
        ship.rect.y = 10
        self.ships.add(ship)


"""
The prep_ships() method creates an empty group, self.ships, to hold the ship instances(line 63).
To fill this group, a loop runs once for every ship the player has left(line 64). Inside the 
loop we create a new ship and set each ship's x-coordinate value so the ships appear next to 
each other with a 10-pixel margin on the left side of the group of ships(line 66).

We set the y-coordinate value 10 pixels down from the top of the screen to the ships line up
with the score image(line 67). Finally, we add each new ship to the group ships(line 68).

Now we need to draw the ships to the screen:
"""
# scorebard.py


def show_score(self):
    --snip--
    self.screen.blit(self.level_image, self.level_rect)

    # Draw ships.
    self.ships.draw(self.screen)


"""
To display the ships on the screen, we call draw() on thr group, and Pygame draws each ship. To
show the player how many ships they have to start with, we call prep_ships() when a new game
starts. We do this in check_play_button() in game_functions.py:
"""

# game_functions.py


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    --snip--

    # Reset the scoreboard images.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()


"""
We also call prep_ships() when a ship is hit to update the display of ship images when the
player loses a ship:
"""

# game_functions.py


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    --snip--

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to the ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()


"""
We first add the parameter sb to the definition of update aliens(line 121). We then pass sb to
ship_hit() [line 126] and check_aliens_bottom() so each has access to the scoreboard object
(line 129).

Then we update the definition of ship_hit() to include sb(line 132). We call prep_ships() after
descreasing the value of ships_left(line 139), so the correct number of ships is displayed each
time a ship is destroyed.

There's a call to ship_hit() in check_aliens_bottom(), so update that function as well:
"""

# game_functions.py


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    --snip--
    # Treat this the same as if the ship got hit.
    ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
    break


"""
Now check_aliens_bottom() accepts sb as a parameter, and we add an sb argument in the call to
ship_hit().

Finally, pass sb in the call to update_aliens() in alien_invasion.py:
"""

# alien_invasion.py

# Start the main loop for the game
while True:
    gf.check_events(ai_settings, screen, stats, sb,
                    play_button, ship, aliens, bullets)

    if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings, screen, stats,
                          sb, ship, aliens, bullets)
        gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

    gf.update_screen(ai_settings, screen, stats, sb, ship,
                     aliens, bullets, play_button)

"""
And thus, the beast is slain! We have successfully created Alien Invasion from scratch.
"""
