import pygame


class Rocket():

    def __init__(self, screen):
        """Initialise Rocket sprite and its starting position."""
        self.screen = screen

        # Load Rocket image + get its rect
        self.image = pygame.image.load(
            'C:/Users/brand/OneDrive/Documents/Web Dev/Python/PCC/Python_Crash_Course_WIP/Part II - Projects/Project 1 - Alien Invasion/Chapter 12 - A Ship that Fires Bullets/Problems/images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start rocket's position to center of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the rocket's center
        self.center = float(self.rect.centerx)

        # movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on  movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        """Draw rocket to its current location."""
        self.screen.blit(self.image, self.rect)
