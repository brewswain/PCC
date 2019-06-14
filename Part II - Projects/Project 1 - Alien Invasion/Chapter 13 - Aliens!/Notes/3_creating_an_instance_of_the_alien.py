"""
Now we create an instance of Alien in alien_invasion.py:
"""

# alien_invasion.py

--snip--
from ship import ship
from alien import Alien


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()
    
    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)

"""
Here we're importing the new Alien class and creating an instance of Alien just before entering
the main while loop. Because we're not changing the alien's position yet, we aren't adding 
anything new inside the loop; however, we do modify the call to update_screen() to pass it the
alien instance.
"""

# Making the Alien Appear Onscreen

"""
To make the alien appear onscreen, we call it's blitme() method in update_screen():
"""

# game_functions.py

def update_screen(ai_settings, screen, ship, bullets):
    --snip--

    ship.blitme()
    alien.blitme()


"""
We draw the alien onscreen after the ship and the bullets have been drawn, so the aliens will be
the top layher of the screen. Now that the first alien appears correctly, we'll write the code to
draw an entire fleet.
"""