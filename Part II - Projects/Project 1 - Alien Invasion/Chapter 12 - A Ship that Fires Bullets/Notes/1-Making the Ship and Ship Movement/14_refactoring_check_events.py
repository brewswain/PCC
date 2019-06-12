"""
The check_events() function will increase in length as we continue to develop the game, so let's break
check_events() into two more functions: One that handles KEYDOWN events and another that handles
KEYUP events:
"""

# game_functions.py


def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = False


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


"""
We make two new functions:
check_keydown_events() and check_keyup_events(). Each needs an event parameter and a ship parameter. The bodies
of these two functions are copied from check_events(), and we've replaced the old code with calls to the new
functions. The check_events() function is simpler now with this cleaner code structure, which will make it 
easier to develop further responses to player input.
"""
