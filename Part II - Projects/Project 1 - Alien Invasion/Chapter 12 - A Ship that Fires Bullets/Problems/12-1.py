import sys
import pygame


def run_window():
    """Initialize game window, and make background blue."""
    pygame.init
    screen = pygame.display.set_mode((1200, 800))

    # Set the background color
    bg_color = (135, 206, 250)

    # Game's main loop.
    while True:

        # Watch for keyboard + mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass of the loop
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_window()
