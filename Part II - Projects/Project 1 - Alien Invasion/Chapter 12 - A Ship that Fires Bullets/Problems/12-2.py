import sys
import pygame
from character import Vivi


def run_window():
    """Initialize game window, and make background blue."""
    pygame.init
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption(
        "VIVI IS THE BEST THANK YOU FOR COMING TO MY TED TALK")

    # Set the background color
    bg_color = (199, 199, 199)

    # Make Vivi
    vivi = Vivi(screen)

    # Game's main loop.
    while True:

        # Watch for keyboard + mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass of the loop
        screen.fill(bg_color)
        vivi.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_window()
