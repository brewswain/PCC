"""
Now let's update alien_invasion.py so it creates a ship and calls the ship's blitme() method:
"""
import sys
import pygame
from settings import Settings
from ship import Ship


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

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()

"""
We import Ship and then make an instance of Ship (named ship) after the screen has been created.
It must come before the main while loop(line 19) so we don't make a new instance of the ship
on each pass through the loop. We draw the ship onscreen by calling ship.blitme() after filling
the background, so the ship appears on top of the background(line 31).

When you run alien_invasion.py now, you should see an empty game screen with our rocket ship
sitting at the bottom center.
"""
