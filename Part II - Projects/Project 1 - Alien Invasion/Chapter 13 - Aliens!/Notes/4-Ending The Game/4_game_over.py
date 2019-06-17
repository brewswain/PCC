"""
Alien Invasion feels more complete now, but the game never ends. The value of ships_left just 
grows increasingly negative. Let's add a game_active flag as an attribute to GameStats to end
the game when the player runs out of ships:
"""

# game_stats.py


def __init__(self, settings):
    --snip--

    # Start Alien Invasion in an active state.
    self.game_active = True


"""
Now we add code to ship_hit() that sets game_active to False if the player has used up all their 
ships:
"""

# game_functions.py


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to the ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships_left.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False


"""
Most of ship_hit() is unchanged. We've moved all of the existing code into an if block, which tests
to make sure the player has at least one ship remaining. If so, we create a new fleet, pause, and
move on. If the player has no ships left, we set game_active to False.
"""
