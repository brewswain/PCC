"""
If we were finished creating a fleet, we'd probably leave create_fleet() as is, but we have
more work to do, so let's clean up the function a bit. Here's create_fleet() with two new
functions: get_number_aliens_x() and create_alien():
"""

# game_functions.py


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and fin the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)

    # Create the first row of aliens..
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)


"""
The body of get_number_aliens_x() is exactly as it was in create_fleet(line 10). The body of
create_alien() is also unchanged from create_fleet() except that we use the alien that was 
just created to get the alien width(line 20).  At line 30 we replace the code for determining
the horizontal spacing with a call to get_number_aliens_x(), and we remove the line referring
to alien_width, because that's now handled inside create_alien()

At line 34 we call create_alien(). This refactoring will make it easier to add new rows and
create an entire fleet.
"""
