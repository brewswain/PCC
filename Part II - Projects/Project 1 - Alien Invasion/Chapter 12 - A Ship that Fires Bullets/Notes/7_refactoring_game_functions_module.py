"""
In larger projects, you'll often refactor code you've written before adding more code. 
Refactoring simplifies the structure of the code you've already written, making it easier 
to build on. In this section we'll create a new module called game_functions, which
will store  a number of functions that make alien invasion work. The game_functions
module will prevent alien_invasion.py from becoming too lengthy and will make the logic
in alien_invasion.py easier to follow.
"""

# The check_events() Function

"""
We'll start by moving the code that manages events to a separate function called 
check_events(). This will simplify run_game() and isolate the event management loop.
Isolating the event loop allows you to manage events separately from other aspects of the 
game, like updating the screen.

Place check_events in a separate module called game_functions:
"""
