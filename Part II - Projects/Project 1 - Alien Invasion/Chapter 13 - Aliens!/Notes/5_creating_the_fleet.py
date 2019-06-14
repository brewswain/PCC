"""
Now we can create the fleet. Here's the new function create_fleet(), which we place at the end
of game_functions.py. We also need to import the Alien class, so make sure you add an import
statement at the top of the file:
"""

from bullet import Bullet
from alien import Alien

--snip--


def create_fleet(ai_settings, screen, aliens):
    """create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Create the first row of aliens..
    for alien_number in range(number_aliens_x):
        # Create an alien and place it in the row.
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


"""
We've already thought through most of this code. We need to know the alien's width and
height in order to place aliens, so we create an alien at line 17 before we perform calculations.
This alien won't be part of the fleet, so don't add it to the group 'aliens'. At line  18 we get 
the alien's width from its rect attribute and store this value in alien_width so we don't have to
keep working through the rect attribute.

At line 19 we calculate the horizontal space available for aliens and the nubmer of aliens that 
can fit into that space. The only change here from our original formulae is that we're using int()
to ensure we end up with an integer number of aliens(line 20) because we don't want to create 
partial aliens, and the range() function needs an integer. The int() function drops the decimal 
part of a number, effectively rounding down. (This is helpful because we'd rather have a little
extra space in each row than an overly crowded row.) 

Next, set up a loop that counts from 0 to the number of aliens we need to make(line 23). In the 
main body of the loop, create a new alien and then set its x-coordinate value to place it in the 
row(line  25). Each alien is pushed to the right one alien width from the left margin.

Next, we multiply the alien width  by 2 to account for the space each alientakes up, including
the empty space to its right, and we multiply this amount by the alien's position in the row.
Then we add each new alien to the group aliens. 

When you run alien Invasion, you should see the first row of aliens appear. The first row is
offset to the left, which is actually good for gameplay because we want the fleet to move 
right until it hits the edge of the screen, then droop down a bit, then move left, and so 
forth. Like the classic game Space Invaders, this movement is more interesting than having
the fleet drop straight down. We'll continue this motion until all aliens are shot down or
until an alien hits the ship or the bottom of the screen.
"""
