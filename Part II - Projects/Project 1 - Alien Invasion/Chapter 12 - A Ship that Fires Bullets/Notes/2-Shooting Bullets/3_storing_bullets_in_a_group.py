"""
Now that we have a Bullet class and the necessary settings defined, we can write code to fire a
bullet each time the player presses the spacebar. First, we'll create a group in alien_invasion.py
to store all the live bullets so we can manage the bullets that have already been fired. This group
will be an instance of the class pygame.sprite.Group, which behaves like a list with some extra
functionality that's helpful when building games. We'll use this group to draw bullets to the screen
on each pass through the main loop and to update each bullet's position:
"""

# alien_invasion.py

import pygame
from pygame.sprite import Group
--snip--


def run_game():
    --snip--
    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()

"""
We import Group from pygame.sprite. At line 23, we make an instance of Group and call it bullets.
This group is created outside of the while loop so we don't create a new group of bullets each time 
the loop cycles.


Note: If you make a group like this inside the loop, you'll be creating thousands of groups of bullets 
and your game will probably slow to a crawl. If your game freezes up, look carefully at what's happening 
in your main while loop.


We pass bullets to check_events() and update_screen(). We'll need to work with bullets in check_events()
when the spacebar is pressed, and we'll need to update the bullets that are being drawn to the screen in
update_screen().

When you call update() on a group(line 30), the group automatically calls update() for each sprite in the 
group. The line 'bullets.update()' calls bullet.update() for each bullet wwe place in the group bullets.
"""
