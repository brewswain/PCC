"""
You can also use a dictionary to store one kind of information
about many objects. For example, if you wnt to poll a number of
people and ask them what their language is, a dictionary is
useful for storing the results.
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favourite language is " +
      favourite_languages['sarah'].title() + '.')

"""
As shown above, we've broken a larger dictionary into several lines. 
Each key is the name of a person who responded to the poll, and 
each value is their language choice. When you know you'll need more
than one line to define a dictionary, use the format above.

Ensure that once you've finished defining the dictionary, you add a 
closing brace on a new line after the last key-value pair. Also, 
it's good practise to include a comma after the last key-value pair
so that you're ready to add  new key-value pair on the next line.
"""
