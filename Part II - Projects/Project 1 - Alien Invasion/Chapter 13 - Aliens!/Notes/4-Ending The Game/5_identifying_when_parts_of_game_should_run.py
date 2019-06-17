"""
In alien_invasion.py we need to identify the parts of the game that should always run and the 
parts that should run only when the game is active:
"""

# alien_invasion.py

while True:
    gf.check_events(ai_settings, screen, ship, bullets)

    if stats.game_active:
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

    gf.update_screen(ai_settings, screen, ship, aliens, bullets)

"""
In the main loop, we always need to call check_events(), even if the game is inactive. For 
example, we still need to know if the user presses Q to quit the game or clicks the button to 
close the window. We also continue updating the screen so we can make changes to the screen
while waiting to see whether the player chooses to start a new game. The rest of the function 
calls only need to happen when the game is active, because when the game is inactive, we don't
need to update the positions of game elements.

Now when you play Alien Invasion, the game should freeze when you've used up all of your ships.
"""
