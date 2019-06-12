"""
Each time we introduce new functionality into our game, we'll typically introduce some new
settings as well. Instead of adding settings throughout the code, let's write a module called
'settings' that contains a class called Settings to store all the settings in one place. This
approach allows us to pass around one settings object instead of many individual settings.
In addition, it makes our function calls simpler and makes it easier to modify the game's
appearance as our project grows. To modify the game, we'll simply change some values in 
settings.py instead of searching for different settings throughout our files.

Here's the initial Settings class:
"""


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

"""
To make an instance of Settings and use it to access our settings, modify alien_invasion.py
as followe:
"""

import sys
import pygame
from settings import Settings


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()


"""
We import Settings into the main program file, and then create an instance of Settings 
and store it in ai_settings after making the call to pygame.init()[Line 37]. 
When we create a screen(line 38), we use the screen_width and screen_height attributes of
ai_settings, and then we use ai_settings to access the background colour when filling the
screen at line 51 as well.
"""