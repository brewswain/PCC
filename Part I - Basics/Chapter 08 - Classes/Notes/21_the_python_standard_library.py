"""
The Python standard library is a set of modules included with every Python installation.
Now that you have a basic understanding of how classes work, you cans tart to use modules
like these that other programmers have written. You can use any function or class in the 
standard library by including a simple import statement at the top of your file. Let's 
look at one class, OrderedDict, from the module collections.

Dictionaries allow you to connect pieces of information, but they don't keep track of the
order in which you add key-value pairs. If you're creating a dictionary and want to keep 
track of the order in which key-value pairs are added, you can use the OrderedDict class
from the collections module. Instances of the OrderedDict class behave almost exactly
like dictionaries except they keep track of the order in which key-value pairs are added.

Let's revisit the favorite_languages.py example  from chapter 6. This time we'll keep
track of the order in which people respond to the poll:
"""

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')


"""
We begin by importing the OrderedDict class from the module collections at line 18. 
At line 20 we create an instance of the OrderedDict class and store this instance in
favorite_languages. Notice nthere are no curly brackets; the call to OrderedDict() 
creates an empty ordered dictionary for us and stores it in favorite_languages. We then
add each name and language to favorite_languages one at a time. Now when we loop through
favorite languages, we know we'll always get responses back in the order they were added:

============================================
|   # Jen's favorite language is Python.   |
|   # Sarah's favorite language is C.      |
|   # Edward's favorite language is Ruby.  |  
|   # Phil's favorite language is Python.  |
============================================

This is a great class to be aware of because it combines the main benefit of lists
(retaining your original order) with the main feature of dictionaries(connecting pieces
of information). As you begin to model real-world situations that you care about, you'll 
probably come across a situation where an ordered dictionary is exactly what you need.
As you learn more about the standard library, you'll become familiar with a number of 
modules like this that'll help you handle common situations.
"""
