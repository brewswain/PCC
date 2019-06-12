"""
We'll start building our game by first creating an empty Pygame window to which 
we can later draw our game elements, such as the ship and the aliens. We'll also 
have our game respond to user input, set the background colour, and load a ship 
image.
"""
# Creating a Pygame Window and Responding to User Input

"""
First, we'll create an empty Pygame window. Here's the basic structure of a game
written in Pygame:
"""




import sys
import pygame
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # Start the main loop for the game
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()

"""
First we import the sys and pygame modules. The pygame module contains the functionality
needed to make a game. We'll use the sys module to exit the game when the player quits.

Alien Invasion starts as the function run_game(). The line pygame.init() at line 21
initializes background settings that Pygame needs to work properly. At line 22, we call
pygame.display.set_mode() to create a display window called screen, on which we'll draw
all of the game's graphical elements. 

The argument (1200, 800) is a tuple that defines the dimensions of the game window. By
passing these dimensions to pygame.display.set_mode(), we create a game window 1200 pixels
wide by 800 pixels high. You can adjust these values depending on the size of your display.

The screen object is called a surface. A surface in Pygame is a part of the screen where you
display a game element. Each element in the game, like the aliens or the ship, is a surface.
The surface returned by display.set_mode() represents the entire game window. When we activate 
the game's animation loop, this surface is automatically redrawn on every pass through the loop.

The game is controlled by a while loop(line 26) that contains an event loop and code that manages
screen updates. An event is an action that the user performs while playing the game, such as
pressing a key or moving  the mouse. To make our program respond to events, we'll write an
event loop to listen for an event and perform an appropriate task depending on the kind of event
that occurred. 

The for loop at line 29 is an event loop.

To access the events detected by Pygame, we'll use the pygame.event.get() method. Any keyboard or
mouse event will cause the for loop to run. Inside the loop, we'll write a series of if statements 
to detect and respond to specific events. For example, when the player clicks the game window's close
button, a pygame.QUIT event is detected and we call sys.exit() to close the game.

The call to pygame.display.flip() at line 34 tells Pygame to make the most recently drawn screen
visible. In this case it draws an empty screen each time through the while loop to erase the old screen
so that only the new screen is visible. When we move the game elements around, pygame.display.flip() will
continually update the display to show the enw positions of elements and hide the old ones, creating the 
illusion of smooth movement.

The last line in this basic game structure calls run_game(), which initializes the game and starts the main
loop. Run this code now, and you should see an empty Pygame window.
"""
