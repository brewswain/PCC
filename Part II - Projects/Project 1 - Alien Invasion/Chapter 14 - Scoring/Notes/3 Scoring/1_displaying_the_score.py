"""
Let's implement a scoring system to track the game's score in real time, as well as to display 
the high score, level, and the number of ships remaining.

The score is a game statistic, so we'll add a score attribute to GameStats:
"""

# game_stats.py


import pygame.font


def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.ships_left = self.ai_settings.ship_limit
    self.score = 0


"""
To reset the score each time a new game starts, we initialize score in reset_stats() rather 
than __init__().
"""

# Displaying the Score

"""
To display the sacore on the screen, we first create a new class, ScoreBoard. For now this 
class will just display the current score, but we'll use it to report the high score, level,
and number of ships remaining as well. Here's the first part of the class; save it as 
scoreboard.py:
"""

# scoreboard.py


class ScoreBoard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()


"""
Because Scoreboard writes text to the screen, we begin by importing the pygame.font module. 
Next, we give __init__() the parameters ai_settings, screen, and stats so it can report the 
values we're tracking(line 38). Then, we set a text color and instantiate a font object
(line 47).

To turn the text to be displayed into an image, we call prep_score() [line 50], which we define
here:
"""
# scoreboard.py


def prep_score(self):
    """Turn the score into a rendered image."""
    score_str = str(self.stats.score)
    self.score_image = self.font.render(
        score_str, True, self.text_color, self.ai_settings.bg_color)

    # Display the score at the top right of the screen.
    self.score_rect = self.score_image.get_rect()
    self.score_rect.right = self.screen_rect.right - 20
    self.score_rect.top = 20


"""
In prep_score(), we first turn the numerical value stats.score into a string(line 69), and then
pass this string to render(), which creates the image(line 70). To display the score clearly 
onscreen, we pass the screen's background color to render() as well as a text color.

We'll position the score in the upper-right corner of the screen and have it expand to the left
as the score increases and the width of the number grows. To make sure the score always lines
up with the right side of the screen, we create a rect called score_rect(line 74) and set its
right edge 20 pixels from the right screen edge(line 75). We then place the top edge 20 pixels
down from the top of the screen(line 76).

Finally, we create a show_score method to display the rendered score image:
"""

# scoreboard.py


def show_score(self):
    """Draw score to the screen."""
    self.screen.blit(self.score_image, self.score_rect)


"""
This method draws the score image to the screen at the location specified by score_rect.
"""
