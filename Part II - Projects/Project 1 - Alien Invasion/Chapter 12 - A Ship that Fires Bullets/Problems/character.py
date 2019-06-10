import pygame


class Vivi():

    def __init__(self, screen):
        """Initialize Vivi's sprite and his starting position."""
        self.screen = screen

        # Load vivi's image and get its rect
        self.image = pygame.image.load(
            'Python_Crash_Course_WIP\Part II - Projects\Project 1 - Alien Invasion\Chapter 12 - A Ship that Fires Bullets\Problems\images\DFFOO_Vivi_Ornitier.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start Vivi at the center of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw Vivi to his current location."""
        self.screen.blit(self.image, self.rect)
