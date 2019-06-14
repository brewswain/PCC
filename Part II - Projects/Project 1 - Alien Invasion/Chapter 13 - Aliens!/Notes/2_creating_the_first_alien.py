"""
Placing one alien on the screen is li8ke placing a ship on the screen. The behavior of each alien
controlled by a class called Alien, which we'll structure like the Ship class. We'll continue
using bitmap images for simplicity.

This image has a gray background, which matches the screen's background color. Make sure to save the
image file you choose in the images folder.

Now we'll write the Alien class:
"""

# alien.py

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(
            'Python_Crash_Course_WIP\Part II - Projects\Project 1 - Alien Invasion\Project Files\images\alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


"""
Most of this class is like the Ship class except for the placement of the alien. We initially place
each alien near the top-left corner of the screen, adding a space to the left of it that's equal to
the alien's width and a space above it equal to its height(line 33).
"""
