"""
You'll often want to run through all entries in a list, performing the same task with each item.  
Here is where loops come in.
In this case, we'll use a for loop.
"""

magicians = ['alice', 'david', 'caroline']
for magician in magicians:  # Pull a name from the list magicians and store it in magician
    print(magician)  # Print the name stored in magician

"""
The set of steps is repeated once for each item in the list, no matter how many items there are.
When writing your own for loops, you can choose any name you want for the temporary variable 
that holds each value in the list.

However, it's useful to choose a name that represents a single item from the list. for example:
for cat in cats:
for dog in dogs:
for item in list_of_items:
"""

# Doing More Work Within a for Loop

magicians = ['alice', 'david', 'caroline']

for magician in magicians:
    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')

print('Thank you, everyone. That was a great magic show!')

"""
Placing the thank you message after the for loop without indentation ensures that it executes
after the loop is completed. This is often a good way to summarize an operation that was 
performed on an entire data set.
"""
