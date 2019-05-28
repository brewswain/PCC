"""
When you no longer need a piece of information that's stored in a dictionary,
you can use the del statement to completely remove a key-value pair. All del
needs is the name of the dictionary and the key that you want to remove.

The deleted Key-value pair is removed permanently, so keep that in mind.
"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
