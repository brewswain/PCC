"""
Currently, the ship moves one pixel per cycle through the while loop, but we can take finer
control of the ship's speed by adding a ship_speed_factor attribute to the Settings class.
We'll use this attribute to determine how far to move the ship on each pass through the
loop. Here's the new attribute in settings.py:
"""

# settings.py


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5


"""
We set the initial value of ship_speed_factor to 1.5. When we want to move the ship, we'll
adjust its position by 1.5 pixels rather than 1 pixel. We're using decimal values for the
speed setting to give us finer control of the ship's speed when we increase the tempo of
the game later on. However, rect attributes such as centerx store only integer values, so 
we need to make some modifications to Ship:
"""

# ship.py


class Ship():

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load(
            'Python_Crash_Course_WIP\Part II - Projects\Project 1 - Alien Invasion\Project Files\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on  movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


"""
At line 36, we add ai_settings to the list of parameters for __init__(), so the ship will have
access to its speed setting. We then turn the ai_settings parameter into an attribute, so we can
use it in update() [line 39]. Now that we're adjusting the position of the ship by fractions of
a pixel, we need to store the position in a variable that can store a decimal value. You can
use a decimal value to set a rect's attribute, but the rect will store only the integer portion
of that value. 

To store the ship's position accurately, we define a new attribute self.center, which can hold
decimal values (line 52). We use the float() function to convert the value of self.rect.centerx 
to a decimal and store this value in self.center.

Now when we change the ship's position in update(), the value of self.center is adjusted by the
amount stored in ai_settings.ship_speed_factor (line 62). After self.center has been updated, we
use the new value to update self.rect.centerx, which controls the position of the ship (line 67).
Only the integer portion of self.center will be stored in self.rect.centerx, but that's fine for
displaying the ship.

We need to pass ai_settings as an argument when we create an instance of Ship in alien_invasion.py:
"""

# alien_invasion.py


def run_game():
    --snip--
    # Make a ship.
    ship = Ship(ai_settings, screen)
    --snip--


"""
Now any value of ship_speed_factor greater than one will make the ship move faster. This will be 
helpful in making the ship respond quickly enough to shoot down aliens, and it will let us change
the tempo of the game as the player progresses in gameplay.
"""
