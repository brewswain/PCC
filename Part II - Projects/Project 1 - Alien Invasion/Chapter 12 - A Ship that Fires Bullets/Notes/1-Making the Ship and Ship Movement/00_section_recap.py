"""
In the next section,we'll add the ability to shoot bullets,, which involves a new file called bullet.py
and some modification to some of the files we already have. Right now, we have four files containing
a number of classes, functions, and methods. To be clear about how the project is organized, let's 
review each of these files before adding more functionality.
"""

# alien_invasion.py

"""
The main file, alien_invasion.py, creates a number of important objects used throughout the game: the 
settings are stored in ai_settings, the main display surface is stored in screen, and a ship instance is
created in this file as well. Also stored in alien_invasion.py is the main loop of the game, which is a
while loop that calls check_events(), ship.update(), and update_screen().

alien_invasion.py is the only file you need to run when you want to play Alien Invasion. The other files:
- settings.py
- game_functions.py
-ship.py

contain code that is imported, directly or indirectly, into this file.
"""

# settings.py

"""
The settings.py file contains the Settings class. This class only has an __init__() method, which initializes
attributes controlling the game's appearance and the ship's speed.
"""

# game_functions.py

"""
The game_functions.py file contains a number of functions that carry out the bulk of the work in the game. The
check_events() function detects relevant events, such as keypresses and releases, and processes each of these
types of events through the helper functions check_keydown_events() and check_keyup_events(). For now, these
functions manage the movement of the ship. The game_functions module also contains update_screen(), which
redraws the screen on each pass through the main loop.
"""

# ship.py

"""
The ship.py file contains the Ship class. Ship has an __init__() method, and update() method to manage the ship's 
position, and a blitme() method to draw the ship to the screen. The actual image of the ship is stored in ship.bmp, 
which is in the images folder.
"""
