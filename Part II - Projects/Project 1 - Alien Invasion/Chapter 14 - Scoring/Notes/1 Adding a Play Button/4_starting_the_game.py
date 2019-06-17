"""
To start a new game when the player clicks Play, add the following code to game_functions.py to
monitor mouse events over the button:
"""

# game_functions.py


def check_events(ai_settings, screen, stats, play_button, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, play_button, mouse_x, mouse_y)


def check_play_button(stats, play_button, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True


"""
We've updated the definition of check_events() to accept the stats and play button parameters.
We'll use stats to access the game_active flag and play_button to check whether the Play button
has been clicked.

Pygame detects a MOUSEBUTTONDOWN event when the player clicks anywhere on the screen(line 18),
but we want to restrict our game to respond to mouse clicks only on th8e Play button. To 
accomplish this, we use pygame.mouse.get_pos(), which returns a tuple containing the x- and y-
coordinates of the mouse cursor when the mouse button is clicked (line 19). We send these 
values to the function check_play_button() [line 20], which uses collidepoint() to see if the 
point of the mouse click overlaps the region defined by the Play button's rect(line 24).
If so, we set game_active to True, and the game begins!

The call to check_events() in alien_invasion.py needs to pass two additional arguments, stats
and play_button:
"""

# alien_invasion.py

while True:
    gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

"""
At this point, you should be able to start and play a full game. When the game ends, the value
of game_active should become False and the Play button should reappear.
"""
