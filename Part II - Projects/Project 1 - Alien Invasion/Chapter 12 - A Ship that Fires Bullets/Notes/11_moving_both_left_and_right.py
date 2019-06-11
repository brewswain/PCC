"""
Now that the ship can move continuously to the right, adding movement to the left is easy. We'll
again modify the Ship class and the check_events() function. Here are the relevant changes to
__init__() and update() in Ship:
"""
# ship.py

       # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on  movement flags."""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

"""
In __init__(), we add a self.moving_left flag. In update(), we use two separate if blocks rather
than an elif in update() to allow the ship's rect.centerx value to be increased and then decreased
if both arrow keys are held down. AThis results in the ship standing still. If we used elif for 
motion to the left, the right arrow key would always have priority. Doing it this way makes the 
movements more accurate when switching from left to right, when the player might momentarily hold
down both keys.

We have to make two adjustments to check_events():
"""

# game_functions.py

def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

