"""
Because the game gets more difficult each time a player reaches a new level, aliens in later 
levels should be worth more points. To implement this functionality, we'll add code to increase
the point value when the game's speed increases:
"""

# settings.py


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        --snip--
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def increase_speed(self):
        """Increase speed settings and alien point values.."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)


"""
We define a rate at which points increase, which we call score_scale(line 19). A small increase
in speed(1.1) makes the game grow challenging quickly, but in order to see a notable difference
in scoring you need to change the alien point value by a larger amount(1.5). Now when we 
increase the speed of the game, we also increase the point value of each hit(line 29). We use
the int() function to increase the point value by whole integers.

To see the value of each alien, add a print statement to the method increase_speed() in
Settings:
"""

# Settings.py


def increase_speed(self):
    --snip--
    self.alien_points = int(self.alien_points * self.score_scale)
    print(self.alien_points)
