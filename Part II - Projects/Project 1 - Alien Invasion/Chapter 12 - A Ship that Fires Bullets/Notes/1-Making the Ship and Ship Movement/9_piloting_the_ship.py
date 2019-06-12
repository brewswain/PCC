"""
Let's give the player the ability to move the ship right and left. To do this, we'll write code
that responds when the player presses the right key/ 'D', or the left arrow key/ 'A'.
We'll focus on movement to the right first, then we'll apply the same principles to control
movement to the lef. As you do this, you'll learn how to control the movement of images on the
screen.
"""

# Responding to a Keypress

"""
Whenever the player presses a key, that keypress is registered in Pygame as an event. Each
event is picked up by the pygame.event.get() method, so we need to specify in our check_events()
function what kind of events to check for. Each keypress is registered as a KEYDOWN event.

When a KEYDOWN event is detected, we need to check whether the key that was pressed  is one
that triggers a certain event. For example, if the right arrow key is pressed, we increase the
ship's rec.centerx value to move the ship to the right:
"""

# game_functions.py




import sys
import pygame
def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or pygame.K_d:
                # Move the ship to the right.
                ship.rect.centerx += 1


"""
We give the check_eventS() function a ship parameter, because the ship needs to move to the
right when the right arrow key/'d' is pressed. Inside check_events() we add an elif block to the
event loop to respond when Pygame detects a KEYDOWN event(line 33). We check if the key pressed is
the right arrow key or 'd', by reading the event.key attribute(line 34). If the key isa pressed, we
move the ship to the right by increasing the value of ship.rect.centerx by 1.

We need to update the call to check_ events()  in alien_invasion.py so it passes ship as an argument:
"""

# alien_invasion.py

# Start the main loop for the game
while True:
    gf.check_events(ship)
    gf.update_screen(ai_settings, screen, ship)

"""
If you run alien_invasion.py now, you should see the ship move to the right one pixel every time you
press the right arrow key. That's a start, but it's not an efficient way to control the ship. Let's
improve this control by allowing continuous movement in the next chapter.
"""
