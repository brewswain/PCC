"""
Sometimes you'll want to store a set of dictionaries in a list,or a list
of items as a value in a dictionary. This is called nesting. You can even
nest a dictionary inside a dictionary.
"""

# A List of Dictionaries

"""
The alien_0 dictionary containts a variety of information about one alien,
but it has no room to store information about a second aliend, much less a 
screen full of aliens. How can you manage a fleet of aliens? One way is to 
make a list of aliens in which each alien is a dictionary of information
about that alien.
"""

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)
print(' ')

"""
A better example would involve more than three aliens, with code that
automatically generates each alien. In the following example, we use
range() to create a fleet of 30 aliens:
"""
# Create Empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Make the first 3 green aliens change to yellow, and yellow into red.
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print('Total number of aliens: ' + str(len(aliens)))

"""
It's common to store a number of dictionaries in a list when each dictionary 
contains many kinds of information about one object. All of the dictionaries 
in the list should have an identical structure so you can loop through the
list and work with each dictionary object in the same way.
"""
