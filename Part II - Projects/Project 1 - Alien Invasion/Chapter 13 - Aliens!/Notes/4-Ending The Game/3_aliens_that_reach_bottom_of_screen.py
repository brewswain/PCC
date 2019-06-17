"""
If an alien reaches the bottom of the screen, we'll respond the same way we do when an alien
hits the ship. Add a new function to perform this check, and call it from update_aliens():
"""

# game_functions.py


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    Check if the feet is at an edge, and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


"""
The function check_aliens_bottom() checks to see whether any aliens have reached the bottom of
the screen. An alien reaches the bottom when its rect.bottom value is greater than or equal to 
the screen's rect.bottom attribute(line 13). If an alien reaches the bottom, we call ship_hit().
If one alien hits the bottom, there's no need to check the rest, so we break out of the loop
after calling ship_hit().

We call check_aliens_bottom() after updating the positions of all the aliens and after looking
for alien-ship collisions(line 31). Now a new fleet will appear every time the ship is hit by
an alien or an alien reaches the bottom of the screen.
"""
