"""
In this section we'll add a play button that appears before a game begins and reappears when
that game ends so the player can play again. 

Right now, the game begins as soon as you run alien_invasion.py. Let's start the game in an
inactive state and then prompt the player to click a Play button to begin. To do this, enter 
the following in game_stats.py:
"""

# game_stats.py


def __init__(self, ai_settings):
    """Initialize statistics."""
    self.ai_settings = ai_settings
    self.reset_stats()

    # Start Alien Invasion in an inactive state.
    self.game_active = False


"""
Now the game should start in an inactive state with no way for the player to start it until we
make a play button.
"""
