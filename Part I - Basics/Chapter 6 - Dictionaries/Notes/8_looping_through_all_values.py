"""
If you're mainly interested in the values that a dictionary contains,
you can use the values() method.

This method returns a list of values without any keys. Using the 
previous dictionary, assume that you want a list of all languages
chosen in our programming language poll without the name of the
person who chose each language.
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('The following languages have been mentioned:')
for language in favourite_languages.values():
    print(language.title())

# Avoiding Repetition by Using Sets
"""
This approach pulls all the values from the dictionary without checking
for repeats. This works well in a small dictionary, but in a poll with a
large number of respondents, this would be a repetitive list.

To see each language chosen without repetition, we can use a set.
A set is similar to a list except that each item in the set must be unique.
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print('\nThe following languages have been mentioned:')
for language in set(favourite_languages.values()):
    print(language.title())
