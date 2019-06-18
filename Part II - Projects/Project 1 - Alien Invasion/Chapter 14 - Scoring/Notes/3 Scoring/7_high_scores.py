"""
Every player wants to beat a game's high score, so let's track and report high scores to give
players something to work toward. We'll store high scores in GameStats:
"""

# game_stats.py


def __init__(self, ai_settings):
    --snip--

    # High score should never be reset.
    self.high_score = 0


"""
Because the high score should never be reset, we initialize high_score in __init__() rather
than in reset_stats().

Now we'll modify Scoreboard to display the high score. Let's start with the __init__() method:
"""

# scoreboard.py


def __init__(self, ai_settings, screen, stats):
    --snip--

    # Prepare the initial score image.
    self.prep_score()
    self.prep_high_score()


"""
The high score will be displayed separately from the score, so we need a new method,
prep_high_score(), to prepare the high score image(line 31).

Here's the prep_high_score() method:
"""

# scoreboard.py


def prep_high_score(self):
    """Turn the high score into a rendered image."""
    high_score = int(round(self.stats.high_score, -1))
    high_score_str = "{:,}".format(high_score)
    self.high_score_image = self.font.render(
        high_score_str, True, self.text_color, self.ai_settings.bg_color)

    # Center the high score at the top of the screen.
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = self.score_rect.top


"""
We round the high score to the nearest 10(line 46) and format it with commas(line 47). We then
generate an image from the high score(line 48), center the high score rect horizontally(line 53)
and set its top attrivute to match the top of the score image(line 54).

The show_score() method now draws the current score at the top right and the high score at the
top center of the screen:
"""

# scoreboard.py


def show_score(self):
    """Draw score to the screen."""
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)


"""
To check for high scores, we'll write a new function, check_high_score(), in game_functions.py:
"""

# game_functions.py


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


"""
The function check_high_score() takes two parameters, stats and sb. It uses stats to check the
current score and the high score, and it needs sb to modify the high score image when necessary.

At line 84, we check the current score against the high score. If the current sacore is greater,
we update the value of high_score and call prep_high_score() to update the image of the high
score.

We need to call check_high_score() each time an alien is hit after updating the score in
check_bullet_alien_collisions():
"""

# game_functions.py


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, swhip, aliens, bullets):
    --snip--

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

        check_high_score(stats, sb)


"""
We call check_high_scores() when the collisions dictionary is present, and we do so after
updating the score for all the aliens that have been hit.

The first time you play Alien Invasion your score will be the high score, so it will be 
displayed as both the current and high score. But when you start a second game, your high score
should appear in the middle and your current score at the right.
"""
