import sys
import pygame


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Event Key Printer")

    bg_color = (199, 199, 199)

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

        screen.fill(bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
