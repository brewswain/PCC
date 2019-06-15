"""
When an alien reaches the edge, the entire fleet needs to drop down and change direction. We
therefore need to make some substantial changes in game_functions.py because that's where we
check to see if any aliens are at the left or right edge. We'll make this happen by writing
the functions check_fleet_edges() and change_fleet_direction)(), and then modifying 
update_aliens():
"""

# game_functions.py


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """
    Check if the feet is at an edge, and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()


"""
If you run the game now, the fleet should move back and forth between the edges of the screen and
drop down every time it hits an edge. Now we can begin shooting down aliens and watch for any 
aliens that hit the ship or reach the bottom the screen.
"""
