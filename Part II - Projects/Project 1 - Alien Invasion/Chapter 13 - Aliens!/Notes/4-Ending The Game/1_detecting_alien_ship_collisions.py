"""
We'll start by checking for collisions between aliens and the ship so we can respond 
appropriately when an alien hits it. We'll check for alien-ship collisions immediately after
updating the position of each alien:
"""

# game_functions.py


def update_aliens(ai_settings, ship, aliens):
    """
    Check if the feet is at an edge, and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")


"""
The method spritecollideany() takes two arguments: a sprite and a group. The method looks for
any member of the group that's collided with the sprite and stays looping through the group
as soon as it finds one member that has collided with the sprite. Here, it loops through the
group aliens and returns the first alien it finds that has collided with ship.

If no collisions occur, spritecollideany() returns None and the if block at line 18 won't
execute. If it finds an alien that's collided with the ship, it returns that alien and the
if block executes: it prints "Ship hit!!!" (line 19). (When an alien hits the ship, we'll
need to do a number of tasks: we'll need to delete all remaining aliens and bullets, recenter 
the ship, and create a new fleet. Before we write code to do all this, we need to know that 
our approach for detecting alien-ship collisions works correctly. Writing a print statement 
is a simple way to ensure that we're detecting collisions properly.)

Now we need to pass ship to update_aliens():
"""

# alien_invasion.py

while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
    gf.update_aliens(ai_settings, ship, aliens)
    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

"""
Now when you run Alien invasion, "Ship hit!!!" should appear in the terminal whenever an alien 
runs into the ship. When testing this feature, setting alien_drop_speed to a higher value
will ensure that aliens reach your ship faster.
"""
