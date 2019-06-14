"""
In game_functions.py, we need  to modify check_keydown_events() to fire a bullet when the player
presses the spacebar. We don't need to change check_keyup_events() because nothing happens when the
spacebar is released. We also need to modify update_screen() to make sure each bullet is drawn to the
screen before we call flip().
"""

# game_functions.py

from bullet import Bullet
--snip--


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        --snip--


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        --snip--
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            --snip--


def update_screen(ai_settings, screen, ship, bullets):
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    --snip--


"""
The group bullets is passed to check_keydown_events(line 13). When the player presses the spacebar,
we create a new bullet(a Bullet instance that we name new_bullet) and add it to the group bullets
(line 16) using the add method; the code bullets.add(new_bullet) stores the new bullet in the group
bullets.

We need to add bullets as a parameter in the definition of check_events() [line 23], and we need to 
pass bullets as an argument in the call to check_keydown_events() as well. We give the bullets 
parameter to update_screen() at line 32, which draws the bullets to the screen. The bullets.sprites()
method returns a list of all sprites in the group bullets. To draw all fired bullets to the screen, we
loop through  the sprites in bullets and call draw_bullet() on each one (line 33).

If you run alien_invasion.py now, you should be able to move the ship right and left, and fire as many 
bullets as you want. The bullets travel up the screen and disappear when they reach the top. You can
alter the size, color, and speed of the bullets in settings.py.
"""
