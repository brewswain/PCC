"""
Let's move the code for firing a bullet to a separate function so we can use a single line of 
code to fire a bullet and keep the elif block in check_keydown_events() simple:
"""

# game_functions.py


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


"""
The function fire_bullet() simply contains the code that was used to fire a bullet when the
spacebar is pressed, and we add a call to fire_bullet() in check_keydown_events() when the
spacebar is pressed.

Run alien_invasion.py one more time and make sure you can satill fire bullets without errors.
"""
