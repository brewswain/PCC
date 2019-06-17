"""
One issue with our Play button is that the button region on the screen will continue to respond
to clicks even when the play button isn't visible. Click the Play button area by accident once 
a game has begun and the game will restart!

To fix this, set the game to start only when game_active is False:
"""

# game_functions.py


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game statistics.
        --snip--


"""
The flag button_clicked stores a True of False value(line 15), and the game will restart only
if Play is clicked AND the game is not currently active(line 16). To test this behavior,
start a enw game and repeatedly click where the play button should be. If everything works as
expected, clicking the Play button area should have no effect on the gameplay.
"""
