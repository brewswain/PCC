"""
We want to know right away when a bullet hits an alien so we can make an alien disappear as
soon as it's hit. To do this, we'll look for collisions immediately after updating a bullet's
position. 

The sprite.groupcollide() method compares each bullet's rect with each alien's rect and 
returns a dictionary containing the bullets and aliens that have collided. Each key in the 
dictionary is a bullet, and the corresponding value is the alien that was hit.
(We'll use this dictionary for scoring later.)

Use this code to check for collisions in the update_bullets() function:
"""

# game_functions.py


def update_bullets(aliens, bullets):
    """Update the position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)


"""
The new line we added loops through each bullet in the group bullets and then loops through
each alien in the group aliens. Whenever the rects of a bullet and alien overlap, groupcollide()
adds a key-value pair to the dictionary it returns. The two True arguments tell Pygame whether
to delete the bullets and aliens that have collided. 
(To make a high powered bullet that's able to travel to the top of the screen, destroying every 
alien in its path, you could set the first Boolean argument to False and keep the second Boolean 
argument set to true. The aliens hit would disappear, but all bullets would stay active until they 
disappeared off the top of the screen.)

We pass thr argument aliens in the call to update_bullets():
"""
