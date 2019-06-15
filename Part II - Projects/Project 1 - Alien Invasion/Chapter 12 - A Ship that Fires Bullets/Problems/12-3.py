import sys
import pygame
from rocket import Rocket


def run_window():
    """Initialize game window, and make background blue."""
    pygame.init
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption(
        "rocket...")

    # Set the background color
    bg_color = (199, 199, 199)

    # Make rocket
    rocket = Rocket(screen)

    # Game's main loop.
    while True:

        # Watch for keyboard + mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event, ship)

            elif event.type == pygame.KEYUP:
                check_keyup_events(event, ship)

        # Redraw the screen during each pass of the loop
        screen.fill(bg_color)
        rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_window()
