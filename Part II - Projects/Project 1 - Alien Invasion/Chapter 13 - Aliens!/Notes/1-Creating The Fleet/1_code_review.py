"""
Although we don't have much cleanup to do right now because we've been refactoring  as we go,
it's annoying to use the mouse to close the game each time we run it to test a new feature.
Let's quickly add a keyboard shortcut to end the game when the user presses Q:
"""

# game_functions.py


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_q:
        sys.exit()


"""
In check_keydown_events() We add a new block that ends the game when Q is pressed. This is a 
fairly safe change because the Q key is far from the arrow keys and the spacebar, so it's unlikely
a player will accidentally press Q and quit the game. Now, when testing, you can press Q to close
the game rather than using your mouse to close the window.
"""
