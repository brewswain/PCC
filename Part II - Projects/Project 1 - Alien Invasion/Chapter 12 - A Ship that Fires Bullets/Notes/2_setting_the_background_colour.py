"""
Pygame creates a black screen by default, but that's boring. Let's set a different colour:
"""

import sys
import pygame


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Set the background color
    bg_color = (230, 230, 230)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()


"""
First, we create a background colour and store it in bg_color(line 16). This colour needs
to be specified only once, so we define its value before entering the main while loop.

Colours in Pygame are specified as RGB colours: a mix of red, green, and blue. Each colour
value can range from 0 to 255. The color value (255, 0, 0) is red, (0, 255, 0) 
is green, and (0, 0, 255) is blue. You can mix RGB values to create 16 million colors. 
The color value (230, 230, 230) mixes equal amounts of red, blue, and green, 
which produces a light gray background color.

At  line 27, we fill a screen with the background colour using the screen.fill() method,
which takes only one argument: a colour.
"""
