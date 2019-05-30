"""
Previously, we used the remove() function to remove a specific value
from a list. The remove() function worked because the value we were
interested in only appeared once in the list. But what if you want
to remove all instances of a value from a list?

In the below example, we have a list of pets with the value 'cat'
repeated several times. To remove all instances of that value, you can 
run a while loop until 'cat' is no longer in the list, as shown here:
"""

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
