"""
The code we just wrote works the first time the player clicks Play but not once the first game
ends, because the conditions that caused the game to end haven't been reset.

To reset the game each time the player clicks Play, we need to reset the game statistics, 
clear our the old aliens and bullets, build a new fleet, and center the ship, as shown here:
"""

# game_functions.py


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
                      bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


"""
We update the definition of check_play_button() so it has access to ai_settings, stats, ship,
aliens, and bullets. It needs these objects to reset the settings that have changed during 
the game and to refresh the visual elements of the game.

At line 17 we reset the game statistics, which gives the player three new ships. Then we set 
game_active to True(so the game will begin as soon as the code in this function finishes 
running), empty the aliens and bullets groups(line 21), and create a new fleet and center the
ship(line 25).

The definition of check_events() needs to be modified, as does the call to check_play_button():
"""

# game_functions.py


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
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
            check_play_button(ai_settings, screen, stats, play_button, ship,
                              aliens, bullets, mouse_x, mouse_y)


"""
The definition of check_events() needs the aliens parameter, which it will pass to 
check_play_button(). We then update the call to check_play_button() so it passes the 
appropriate arguments(line 56).

Now update the call to check_events() in alien_invasion.py so it passes the aliens argument:
"""

# alien_invasion.py
while True:
    gf.check_events(ai_settings, screen, stats,
                    play_button, ship, aliens, bullets)

"""
The game will now reset properly each time you click Play, allowing you to play it as many times 
as you want!
"""
