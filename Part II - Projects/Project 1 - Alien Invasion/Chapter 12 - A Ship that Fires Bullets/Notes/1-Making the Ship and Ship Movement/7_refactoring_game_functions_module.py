"""
In larger projects, you'll often refactor code you've written before adding more code. 
Refactoring simplifies the structure of the code you've already written, making it easier 
to build on. In this section we'll create a new module called game_functions, which
will store  a number of functions that make alien invasion work. The game_functions
module will prevent alien_invasion.py from becoming too lengthy and will make the logic
in alien_invasion.py easier to follow.
"""

# The check_events() Function

"""
We'll start by moving the code that manages events to a separate function called 
check_events(). This will simplify run_game() and isolate the event management loop.
Isolating the event loop allows you to manage events separately from other aspects of the 
game, like updating the screen.

Place check_events in a separate module called game_functions:
"""




import pygame
import sys
def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

"""
This module imports sys and pygame, which are used in the event checking loop. The function
needs no parameters at this point, and the body is copied from the event loop alien_invasion.py.

Now let's modify alien_invasion.py so it imports the game_functions module, and we'll replace 
the event loop with a call to check_events():
"""

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


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

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()

"""
We no longer need to import sys directly into the main program file, because it's only being
used in the game_functions module now. We give the imported game_functions module the alias
gf for simplification.
"""