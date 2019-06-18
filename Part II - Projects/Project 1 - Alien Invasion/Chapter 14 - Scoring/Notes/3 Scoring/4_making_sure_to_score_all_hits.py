"""
As currently written, our code could miss some aliens. For example, if two bullets collide with
aliens during the same pass through the loop or if we make an extra wide bullet to hit 
multiple aliens, the player will receive points only for one of the alines killed. To fix this,
let's refine the way that alien bullet collisions are detected.

In check_bullet_alien_collisions(), any bullet that collides with an alien becomes a key in the
collisions dictionary. The value associated with each bullet is a list of aliens it has collided
with. We loop through the collisions dictionary to make sure we award points for each alien
hit:
"""

# game_functions.py


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""

    # # Remove any bullets and aliens that have collided.
    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    # Debug mode SuperBullet
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()


"""
If the collisions dictionary has been defined, we loop through all values in the collisions 
dictionary. Remember that each value is a list of aliens hit by a single bullet. We multiply
the value of each alien by the number of aliens in each list and add this amount to the current
score.
"""
