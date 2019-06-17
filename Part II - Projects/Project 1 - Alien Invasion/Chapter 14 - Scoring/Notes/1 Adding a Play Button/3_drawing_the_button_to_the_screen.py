"""
We'll use the Button class to create a Play button. Because we need only one Play button, we'll
create the button directly in alien_invasion.py as shown here:
"""

# alien_invasion.py

--snip--
from game import GameState
from button import Button
--snip--


pygame.display.set_caption("Alien Invasion")

# Make the play button.
play_button = Button(ai_settings, screen, "Play")
--snip--

while True:
    --snip--
    gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

"""
We import Button and create an instance called play_button(line 17), and then we pass 
play_button to update-screen() so the button appears when the screen updates (line 22).

Next, modify update_screen() so the Play button appears only when the game is inactive:
"""

# game_functions.py

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    --snip--

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()

"""
To make the Play button visible above all other elements on the screen, we draw it after all 
other game elements have been drawn and before flipping to a new screen. Now when you run 
Alien Invasion you should see a Play button in the center of the screen.
"""