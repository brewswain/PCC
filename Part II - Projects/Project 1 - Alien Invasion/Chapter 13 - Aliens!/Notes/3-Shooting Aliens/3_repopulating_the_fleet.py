"""
One key feature of Alien Invasion is that that the aliens are relentless: every time the fleet is
destroyed, a new fleet should appear.

To make a new fleet of aliens appear after a fleet has been destroyed, first check to see whether
the group aliens is empty. If it is, we call create_fleet(). We'll perform this check in
update_bullets() because that's where individual aliens are destroyed:
"""

# game_functions.py


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Update the position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # Destroy existing bullets and create new flee.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


"""
At line 27 we check whether the group aliens is empty. If it is, we get rid of any existing bullets
by using the empty() method, which removes all the remaining sprites from a group(line 29). We also
call create_fleet(), which fills the screen with aliens again.

The definition of update_bullets() now has the additional parameters ai_settings, screen, and ship,
so we need to update the call to update_bullets() in alien_invasion.py:
"""

# alien_invasion.py

while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

"""
Now a new fleet appears as soon as you destroy the current fleet.
"""
