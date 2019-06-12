"""
Lets move the code for updating the screen to a separate function called update_screen() in
game_functions.py to further simplify run_game():
"""

import game_functions as gf
from ship import Ship
from settings import Settings
import sys

import pygame


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()


"""
The new update_screen() function takes three parameters: ait_settings, screen, and ship.
Now we need to update the while loop from alien_invasion.py with a call to update_screen():
"""


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        gf.check_events()
        gr.update_screen(ai_settings, screen, ship)


run_game()

"""
These two functions make the while loop simpler and will make further development easier.
Instead of working inside run_game(), we can do most of our work in the module 
game_functions.

Because we wanted to start out working with code ina  single file, we didn't introduce
the game_functions module right away. This approach gives you an idea of a realistic
development process: You start out writing your code as simply as possible, and refactor 
it as your project becomes more complex.

Now that our code is restructured to make it easier to add to, we can work on the dynamic
aspects of the game!
"""
