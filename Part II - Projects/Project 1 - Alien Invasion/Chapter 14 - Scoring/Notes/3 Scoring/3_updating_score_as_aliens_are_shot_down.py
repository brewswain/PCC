"""
To write a live score to the screen, we update the value of stats.score whenever an alien is 
hit, and then call prep_score() to update the score image. But first, let's determine how many
points a player gets each time they shoot down an alien:
"""

# settings.py


def initialize_dynamic_settings(self):
    --snip--

    # Scoring
    self.alien_points = 50


"""
We'll increase the point value of each alien as the game progresses. To make sure this point
value is reset each time a new game starts, we set the value in initialize_dynamic_settings().

Update the score each time an alien is shot down in check_bullet_alien_collisions():
"""

# game_functions.py


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""

    # # Remove any bullets and aliens that have collided.
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Debug mode SuperBullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        stats.score += ai_settings.alien_points
        sb.prep_score()


"""
We update the definition of check_bullet_alien_collisions() to include the stats and sb
parameters so it can update the score and the scoreboard. When a  bullet hits an alien, 
Pygames returns a collisions dictionary. We check whether the dictionary exists, and if it
does, the alien's value is added to the score(line 37). We then call prep_score() to create a 
new image for the updated score.

We need to modify update_bullets() to make sure the appropriate arguments are passed between
functions:
"""
# game_functions.py


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update the position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(
        ai_settings, screen, stats, sb, ship, aliens, bullets)


"""
The definition of update_bullets() needs the additional parameters stats and sb. The call to
check_bullet_alien_collisions() needs to include the stats and sb arguments as well.

We also need to modify the call to update_bullets() in the main while loop:
"""

# alien_invasion.py

# Start the main loop for the game
while True:
        gf.check_events(ai_settings, screen, stats,
                        play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship,
                         aliens, bullets, play_button)

"""
The call to update_bullets() needs the stats and sb arguments. Now when you play Alien Invasion
you should be able to rack up points!
"""
