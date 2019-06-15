"""
To finish the fleet, determine the number of rows that fit on the screen and then repeat the
loop( for creating the aliens in one row) that number of times. To determine the number of
rows, we find the available vertical space by subtracting the alien height from the top, the
ship height from the bottom, and two alien heights from the bottom of the screen:

=====================================================================================
|   available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height  |
=====================================================================================

The result will create some empty space above the ship, so the player has some time to start
shooting aliens at the beginning of each level. Each row needs some empty space below it, 
which we'll make equal to the height of one alien. To find the number of rows, we divide the
available space by two times the height of an alien. (Again, if these calculations are off, 
we'll see it right away and adjust until we have reasonable spacing.)

===========================================================
|   number_rows = available_height_y / (2* alien_height)  |
===========================================================

Now that we know how many rows fit in a fleet, we can repeat the code for creating a row:
"""

# game_functions.py


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_height_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship,  aliens):
    """Create a full fleet of aliens."""
    # Create an alien and fin the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens..
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number, row_number)


"""
To calculate the number of tows that we can fit on the screen, we write our 
available_space_y and number_rows calculations into the function get_number_rows(line 27), 
which is similar to get_number_aliens_x(). The calculation is wrapped in parentheses so 
the outcome can be split over two lines, which results in lines of 70 characters or less 
as is recommended(line 29). We use int() because we don't want to create a partial row of 
aliens.

To create multiple rows, we use two nested loops: one outer and one inner loop(line 54). The
inner loop creates the aliens in one row. The outer loop counts from 0 to the number of rows 
we want; Python will use the code for making a single row and repeat it number_rows times.

To nest the loops, write the new for loop and indent the code you want to repeat. Now when
we call create-alien(), we include an argument for the row_number so each row can be placed
farther down the screen.

The definition of create_alien() needs a parameter to hold the row number. Within create_alien(),
we change an alien's y-coordinate value when it's not in the first row(line 41) by starting with 
one's alien height to create empty space at the top of the screen. Each row starts two alien 
heights below the last row, so we multiply the alien height by two and then by the row number.
The first row number is 0, so the vertical placement of the first row is unchanged. All 
subsequent rows are placed further down the screen.

The definition of create_fleet() also has a new parameter for the ship object, which means we
need to include the ship argument in the call to create_fleet() in alien_invasion.py:
"""

# alien_invasion.py


# Create the fleet of aliens.
gf.create_fleet(ai_settings, screen, ship, aliens)
