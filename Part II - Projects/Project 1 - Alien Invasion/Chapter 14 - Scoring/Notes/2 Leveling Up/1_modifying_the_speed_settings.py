"""
We'll first reorganize the Settings class to group the game settings into static and changing
ones. We'll also make sure that settings that change over the course of a game reset when
we start a new game. Here's the __init__() method for settings.py:
"""

# settings.py


def __init__(self):
    """Initialize the game's static settings."""
    --snip--

    # Alien settings
    self.alien_speed_factor = 1
    # self.fleet_drop_speed = 10

    # How quickly the game speeds up
    self.speedup_scale == 1.1

    self.initialize_dynamic_settings()

    # fleet_direction of 1 represents rights; -1 represents left.
    self.fleet_direction = 1


"""
We continue to initialize the settings that stay constant in the __init__() method. At line 43
we add a speedup_scale setting to control how quickly the game speeds up: A value of 2 will
double the game speed every time the player reaches a new level; a value of 1 will keep the
speed constant. A speed value like 1.1 should increase the speed enough to make the game
challenging but not impossible. Finally, we call initialize_dynamic_settings() to initialize
the values for attributes that need to change throughout the course of a game(line 45).

Here's the code for initialize_dynamic_settings():
"""

# settings.py


def initialize_dynamic_settings(self):
    """Initialize settings that change throughout the game."""
    self.ship_speed_factor = 1.5
    self.bullet_speed_factor = 3
    self.alien_speed_factor = 1

    # fleet_direction of 1 represents rights; -1 represents left.
    self.fleet_direction = 1


"""
This method sets the initial values for the ship, bullet, and alien speeds. We'll increase
these speeds as the player progresses in the game and reset them each time the player starts
a new game. We include fleet_direction in this method so the aliens always move right at the
beginning of a new game. To increase the speeds of the ship, bullets, and aliens each time the
player reaches a new level, use increase_speed():
"""

# settings.py


def increase_speed(self):
    """Increase speed settings."""
    self.ship_speed_factor *= self.speedup_scale
    self.bullet_speed_factor *= self.speedup_scale
    self.alien_speed_factor *= self.speedup_scale


"""
To increase the speed of these game elements, we multiply each speed setting by the value of
speedup_scale.

We increase the game's tempo by calling increase_speed() in check_bullet_alien_collisions()
when the last alien in a fleet has been shot down but before creating a new fleet:
"""

# game_functions.py


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    --snip--

    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create new fleet.
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


"""
Changing the values of the speed settings ship_speed_factor, alien-speed_factor, and 
bullet_speed_factor is enough to speed up the entire game!
"""
