"""
The keys() method is useful when you don't need to work with all of the values
in a dictionary. Let's loop through the favourite_languages dictionary and print
the names of everyone who took the pool:
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in favourite_languages.keys():
    print(name.title())

"""
Looping through the keys is actually the  default behaviour when looping through 
a dictionary, so this code would have had the same output if you wrote:

        for name in favourite_languages:

You can choose to use the keys() method explicitly if it makes your code easier
to read, or omit it if you wish.



You can access the value associated with any key you care about inside the loop by 
using the current key. Let's print a message to a couple of friends about the
languages they chose. We'll loop through the names in the dictionary, but when the
name matches one of our friends, we'll display a message about their fave language.
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        print("\tHi " + name.title() + '. I see your favourite language is ' +
              favourite_languages[name].title() + '!')
