"""
We want the mouse cursor visible in order to begin play, but once play begins it only gets in
the way. To fix this, we'll make it invisible once the game becomes active:
"""

# game_functions.py


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)


"""
Passing False to set_visible() tells Pygame to hide the cursor when the mouse is over the game
window. 

We'll make the cursor reappear once the game ends so the player can click Play to begin a new
game. Here's the code to do that:
"""

# game_functions.py


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to the ship being hit by alien."""
    if stats.ships_left > 0:
        --snip--

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


"""
We make the cursor visible again as soon as the game becomes inactive, which happens in 
ship_hit(). Attention to details like this makes your game seem more professional and allows
the player to focus onh playing rather than figuring out the user interface.
"""
