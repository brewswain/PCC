"""
After choosing an image for the ship, we need to diplay it onscreen. To use our ship, we'll 
write a module called ship, which contains the class Ship. This class will manage most of
the behaviour of the player's ship:
"""

import pygame


class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load(
            'Python_Crash_Course_WIP\Part II - Projects\Project 1 - Alien Invasion\Project Files\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


"""
First, we import the pygame module. The __init__() method of Ship takes two parameters: the self
reference and the screen where we'll draw the ship. 
To load the image, we call pygame.image.load() [line 17]. This function returns a surface 
representing the ship, which we store in self.image.

Once the image is loaded, we use get_rect() to access the surface's rect attribute(line 18).
One reason why Pygame is so efficient is that it lets you treat game elements like rectangles
(rects), even if they're not exactly shaped like rectangles. Treating an element as a rectangle
is efficient because rectangles are simple geometric shapes. This approach usually works well
enough that no one playing the game will notice that we're not working with the exact shape
of each game element.

When you're centering a game element, work with the center, centerx, or centery attributes of
a rect. When you're working at an edge of the screen, work with the top, bottom, left, or right
attributes. When you're adjusting the horizontal or vertical placement of the rect, you can 
just use the x and y attributes, which are the x- and y-coordinates of its top-left corner. 
These attributes spare you from having to do calculations that game developers formerly had 
to do manually, and you'll find you'll use them often.

In Pygame, the origin(0,0) is at the top-left corner of the screen, and coordinates increase as
you go down and right. on a 1200 x 800 screen, the origin is at the top-left corner, and the
bottom-right corner has the coordinates (1200,800).

We'll position the ship at the bottom center of the screen. To do so, first store the screen's
rect in self.screen_rect(line 19), and then make the value of self.rect.centerx
(The x-coordinate of the ship's center) match the centerx attribute of the screen's rect
(line 22). Make the value of self.rect.bottom(The y-coordinate of the ship's bottom) equal to
the value of the screen rect's bottom attribute. Pygame will use these rect attributes to 
position the ship image so it's centered horizontally and aligned with the bottom of the
screen.

At line 25 we define the blitme() method, which will draw the image to the screen at the 
position specified by self.rect.
"""
