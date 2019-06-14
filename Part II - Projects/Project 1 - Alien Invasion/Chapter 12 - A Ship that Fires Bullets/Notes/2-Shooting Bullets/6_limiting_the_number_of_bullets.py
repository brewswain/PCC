"""
Many shooting games limit the number of bullets a player can have on screen at one time to
encourage players to shoot accurately. We'll do the same in Alien Invasion.

First, store the number of bullets allowed in settings.py:
"""
# settings.py

self.bullet_speed_factor = 1
self.bullet_width = 3
self.bullet_height = 15
self.bullet_color = 60, 60, 60
self.bullets_allowed = 5

"""
This limits the player to five bullets at a time. We'll use this setting in game_functions.py
to check how many bullets exist before creating a enw bullet in check_keydown_events():
"""

# game_functions.py

elif event.key == pygame.K_SPACE:
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

"""
When the spacebar is pressed, we check the length of bullets. If len(bullets) is less than five,
we create a new bullet. But if five bullets are already active, nothing happens when the spacebar
is pressed. If you run the game now, you should be able to fire bullets only in groups of five.
"""
