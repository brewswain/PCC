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

        print("Hi " + name.title() + '. I see your favourite language is ' +
              favourite_languages[name].title() + '!')


"""
You can also use the keys() method to find out if a particular person was polled. 
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favourite_languages.keys():
    print("\nErin, please take our poll!")


# Looping Through a Dictionary's Keys in Order

"""
A dictionary always maintains a clear connection between each key and its associated value,
but the items aren't sorted into a predictable order. That's not a problem, since you usually 
just want to obtain the correct value associated with each key.

One way to return items in a certain order is to sort the keys as they're returned,
in the for loop. You can use the sorter() function to get a copy of the keys in order
"""

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favourite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')


"""
The sorted() function around the dictionary.keys() method tells Python to list all keys
in the dictionary and sort that list before looping through it. The output shows everyone
who took the poll with the names displayed in order:
"""
