"""
Because Pygame doesn't have a built-in method for making buttons, we'll write a Button class
to create a filled rectangle with a label. You can use this code to make any button in a game.
Here's the first part of the Button class:
"""

# button.py

import pygame.font


class Button:

    def __init__(self, ai_settings, screen, message):
        """Initialise button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self.prep_message(message)


"""
First we import the pygame.font module, which lets Pygame render text to the screen. The 
__init__() method takes the parameters self, the ai_settings and screen objects, and message, 
which contains the text for the button(line 14). We set the button dimensions at line 20, and 
then we set button_color to color the button's rect object bright green and set text_color to
render the text in white.

At line 23 we prepare a font attribute for rendering text. The None argument tells Pygame to
use the default font, and 48 determines the size of the text. To center the button on the 
screen, we create a rect for the button (line 26) and set its center attribute to match that
of the screen.

Pygame works with text by rendering the string you want to display as an image. At line 30 we
call prep_message() to handle this rendering.

Here's the code for prep_message():
"""

# button.py


def prep_message(self, message):
    """Turn message into a rendered image and center text on the button."""
    self.message_image = self.font.render(
        message, True, self.text_color, self.button_color)
    self.message_image_rect = self.message_image.get_rect()
    self.message_image_rect.center = self.rect.center


"""
The prep_message() method needs a self parameter and the text to be rendered as an image
(message). The call to font.render() turns the text stored into message into an image, which
we then store in message_image(line 56). The font.render() method also takes a Boolean value to
turn antialiasing on or off. The remaining arguments are the specified font color and 
background color. We set antialiasing to True and set the text background to the same color as
the button. (If you don't include a background color, Pygame will try to render the font with a
transparent background.)

At line 58, we center the text image on the button by creating a rect from the image and 
setting its center attribute to match that of the button.

Finally, we create a draw_button() method that we can call to display the button onscreen:
"""

# button.py


def draw_button(self):
    """Draw blank button and then draw message."""
    self.screen.fill(self.button_color, self.rect)
    self.screen.blit(self.message_image, self.message_image_rect)


"""
We call screen.fill() to draw the rectangular portion of the button. Then we call screen.blit()
to draw the text image to the screen, passing it an image and the rect object associated with
the image. This completes the Button class.
"""
