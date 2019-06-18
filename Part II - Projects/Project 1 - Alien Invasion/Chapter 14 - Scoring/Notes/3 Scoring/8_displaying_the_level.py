"""
To display the player's level in the game, we first need an attribute in GameStats representing
the current level. To reset the level at the start of each new game, initialize it in
reset_stats():
"""

# game_stats.py


def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.ships_left = self.ai_settings.ship_limit
    self.score = 0
    self.level = 1


"""
To have Scoreboard display the current level(just below the current score), we call a new
method, prep_level(), from __init__():
"""

# scoreboard.py


def __init__(self, ai_settings, screen, stats):
    --snip--

    # Prepare the initial score images.
    self.prep_score()
    self.prep_high_score()
    self.prep_level()


"""
Here's prep_level():
"""

# scoreboard.py


def prep_level(self):
    """Turn the level into a rendered image."""
    self.level_image = self.font.render(
        str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

    # Position the level below the score.
    self.level_rect = self.level_image.get_rect
    self.level_rect.right = self.score_rect.right
    self.level_rect.top = self.score_rect.bottom + 10


"""
The method prep_level() creates an image from the value stored in stats.level(line 43) and sets
the image's right attribute to match the score's right attribute(line 48). It then sets the top
attribute 10 pixels beneath the bottom of the score image to leave space between the score and
the level(line 49).

We also need to update show_score():
"""

# scoreboard.py


def show_score(self):
    """Draw score and ships to the screen."""
    self.screen.blit(self.score_image, self.score_rect)
    self.screen.blit(self.high_score_image, self.high_score_rect)
    self.screen.blit(self.level_image, self.level_rect)


"""
This adds a line to draw the level image to the screen.

We'll increment stats.level and update the level image in check_bullet_alien_collisions():
"""

# game_functions.py


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    --snip--

    if len(aliens) == 0:
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        ai_settings.increase_speed()

        # Increase level.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


"""
If a fleet is destroyed, we increment the value of stats.level(line 89) and call prep_level() 
to make sure the new level is displayed correctly(line 90).

To make sure the scoring and level images are updated properly at the start of a new game, 
trigger a reset when the Play button is clicked:
"""

# game_functions.py


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):

    --snip--

    # Reset the game statistics.
    stats.reset_stats()
    stats.game_active = True

    # Reset the scoreboard images.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()

    --snip--


"""
The definition of check_play_button() needs the sb object. To reset the scoreboard images, we
call prep_score(), prep_high_score(), and prep_level() after resetting the relevant game
settings(line 116).

Now we pass sb from check_events() so check_play_button() has access to the scoreboard object:
"""

# game_functions.py


def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)


"""
The definition of check_events() needs sb as a parameter, so the call to check_play_button() 
can include sb as an argument(line 145).

Finally, update the call to check_events() in alien_invasion.py so it passes sb as well:
"""

# alien_invasion.py

# Start the main loop for the game
while True:
    gf.check_events(ai_settings, screen, stats, sb,
                    play_button, ship, aliens, bullets)

"""
Now you can see how many levels you 've completed.
"""
