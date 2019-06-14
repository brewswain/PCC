""" 
At the moment, the bullets disappear when they reach the top, but only because Pygame can't
draw them above the top of the screen. The bullets actually continue to exist; their 
y-coordinate values just grow increasingly negative. This is a problem, because they continue 
to consume memory and processing power.

We need to get rid of these old bullets, or the game will slow down from doing sao much unnecessary 
work. To do this, we need to detect when the bottom value of a bullet's rect has a value of 0, 
which indicates the bullet has passed off the top of the screen:
"""
# alien_invasion.py

while True:
    ships.update()
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

"""
You shouldn't remove items from a list or group within a for loop, so we have to loop over a copy
of the group. We use the copy() method to setup the for loop(line 18), which enables us to modify
bullets inside the loop. We check each bullet to see whether it has disappeared off the top of the
screen at line 19. If it has, we remove it from bullets (line 20). At line 21, we insert a print
statement to show how many bullets currently exist in the game and verify that they're being
deleted.

If this code works correctly, we can watch the terminal output while firing bullets and see that 
the number of bullets decreases to zero after each set of bullets has cleared the top of the screen.
After you run the game and verify that bullets are deleted properly, remove the print statement. If 
you leave it in, the game will slow down significantly because it takes more time to write output
to the terminal than it does to draw graphics to the game window.
"""
