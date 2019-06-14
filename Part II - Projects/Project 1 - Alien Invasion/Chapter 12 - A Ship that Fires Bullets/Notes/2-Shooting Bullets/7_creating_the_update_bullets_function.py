"""
We want ot keep our main alien_invasion.py program file as simple as possible, so now that
we've written adn checked the bullet management code we can move it to the game_functions
module. We'll create a new function called update_bullets() and add it to the end of
game_functions.py:
"""

# game_functions.py


def update_bullets(bullets):
    """Update the position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


"""
The code for update_bullets() is simply cut and pasted from alien_invasion.py; the only 
parameter it needs is the group bullets.

The while loop in alien_invasion.py looks simple again:
"""

# alien_invasion.py

# Start the main loop for the game
while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_settings, screen, ship, bullets)

"""
We've made it so our main loop contains only minimal code so we can quickly read the 
function names and understand what's happening in the game. The main loop checks for player
input at line 22, and then it updates the position of the ship at line 34 and any bullets
that have been fired at line 35. We then use the updated positions to draw a new screen at 
line 36.
"""
