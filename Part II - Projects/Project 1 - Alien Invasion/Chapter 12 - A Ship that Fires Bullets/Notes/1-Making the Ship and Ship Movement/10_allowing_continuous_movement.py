"""
When the player holds down the right arrow/D key, we want the ship to continue moving right
until the player releases the key. We'll have our game detect a pygame.KEYUP event so we'll
know when the right arrow key is released; then we'll use the KEYDOWN and KEYUP events
together with a flag called moving_right to implement continuous movement.

When the ship is motionless, the moving_right flag will be False. When the right arrow key
is pressed, we'll set the flag to True, and when it's released, we'll set the flag to False
again.

The Ship class controlls all attributes of the ship, so we'll give it an attribute called 
moving_right and an update() method to check the status of the moving_right flag. The
update() method will change the position of the ship if the flag is set ot True. We'll 
call this method any time we want to update the position of the ship. 

Here are the changes to the Ship class:
"""
# ship.py


class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load(
            'Python_Crash_Course_WIP\Part II - Projects\Project 1 - Alien Invasion\Project Files\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


"""
We add a self.moving_right attribute in the __init__() method and set it to False initially(line 37).
Then we add update(), which moves the ship right if the flag is True(line 44).

Now, we modify check_events() so that moving_right is set to True when the right arrow key is pressed
and False when the key is released:
"""
# game_functions.py


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or pygame.K_d:
                # Move the ship to the right.
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_d:
                ship.moving_right = False


"""
At line 68, we modify how the game responds when the player presses the right arrow key: Instead of
changing the ship's position directly, we merely set moving_right  to True. At line 70, we add a new
elif block, which responds to KEYUP events. When the player releases the right arrow key/D, we set
moving_right to False. 

Finally, we modify the while loop in alien_invasion.py so it calls the ship's update() method on each
pass through the loop:
"""
# alien_invasion.py

# Start the main loop for the game
while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

"""
The ship's position will update after we've checked for keyboard events and before we update the screen.
This allows the ship's position to be updated in response to player input and ensures the updated
position is used when drawing the ship to the screen.

When you run alien_invasion.py and hold down the right arrow key, the ship should move continuously to the 
right until you release the key.
"""
