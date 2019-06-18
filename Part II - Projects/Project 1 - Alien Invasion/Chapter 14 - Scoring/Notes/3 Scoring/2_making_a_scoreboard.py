"""
To display the score, we'll create a Scoreboard instance in alien_invasion.py:
"""

# alien_invasion.py

from game_stats import GameStats
from scoreboard import Scoreboard
--snip--


def run game():
    --snip--
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    --snip--
    # Start the main loop for the game.
    while True:
        --snip--
        gf.update_screen(ai_settings, screen, stats, sb,
                         ship, aliens, bullets, play_buttons)


run_game()

"""
We import the new Scoreboard class and make an instance called sb after creating the stats 
instance(line 16). We then pass sb to update_screen() so the score can be drawn to the screen
(line 21). 

To display the score, modify update_screen() like this:
"""

# game_functions.py


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_buttons):
    --snip--
    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive
    --snip--


"""
We add sb to the list of parameters that define update_screen() and call show_score() just 
before the Play button is drawn.

Now, Alien Invasion should have '0' displayed at the top right of the screen.
"""
