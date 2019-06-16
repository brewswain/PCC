"""
Let's refactor update_bullets() so it's not doing so many different tasks. We'll move the code 
for dealing with bullet-alien collisions to a separate function:
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

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""

    # # Remove any bullets and aliens that have collided.
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Debug mode SuperBullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if len(aliens) == 0:
        # Destroy existing bullets and create new flee.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


"""
We've created a new function, check_bullet_alien_collisions, to look for collisions between
bullets and aliens, and to respond appropriately if the entire fleet has been destroyed. This 
keeps update_bullets() from growing too long and simplifies further development.
"""
