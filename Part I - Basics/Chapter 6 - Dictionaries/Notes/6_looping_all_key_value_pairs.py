"""
A single Python dictionary can contain just a few key-value pairs or millions of pairs.
Since a dictionary can contain large amounts of data, Python lets you loop through a
dictionary. Dictionaries can be used to store information in a variety of ways; 
thus, several different ways exist to loop through them. You can loop through
all of a dictionary's key-value pairs, through its keys, or through its values.
"""


# Looping Through All Key-Value Pairs


"""
Let's consider a new dictionary designed to store information about a user on a website.
The dictionary would store the user's username, first name, and last name.
If you wanted to see everything stored in this user's dictionary, you could loop through
the entire dictionary by using a for loop.

As seen below, the items() method returns a list of key-value pairs.
"""
user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}

# Create names for the two variables that will hold the key and value in each key-value pair.
# Then, include the name of the dictionary followed by the items() method, which returns a list of key-value pairs.
# The for loop then stores each of these pairs in the two variables provided.
for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)


"""
Generally speaking, Python does not care about the order in which key-value pairs are stored; it only 
tracks the connections between individual keys and their values. This comes in particularly well for 
dictionaries like the favourite_languages one we did in 5_dictionary_of_similar_objects.py, which 
stores the same kind of information for many different keys.

Since the keys always refer to a person's name and the value is always a language, we can use the 
variables name and language respectively in the loop instead of 'key' and 'value'.
"""
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('\n')
for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + '.')
