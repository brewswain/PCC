"""
Sometimes, instead of putting a dictionary inside a list, it's
useful to put a list inside a dictionary.  For example, consider
how you might describe a pizza that someone is ordering. If 
you only used a list, all you could probably store is a list of 
toppings. With a dictionary, a list of stoppings can be just 
one aspect of the pizza you're describing.
"""

# Store information about a pizza  being ordered.

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarise the order.
print("you ordered a " + pizza['crust'] +
      '-crust pizza ' + "with the following toppings:")

for topping in pizza['toppings']:
    print('\t' + topping)

"""
You can nest a list inside a dictionary any time you want more
than one value to be associated with a single key in a dictionary.
In the earlier example of favourite programming languages, if we 
were to store each person's responses in a list, people could choose more
than one favourite language. When we loop through the dictionary, the 
value associated with each person would be a list of languages rather
than a single language.

Inside the dictionary's for loop, we use another for loop to run through
the list of languages associated with each person:
"""

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sara': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favourite_languages.items():
    print("\n" + name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())


"""
You should not nest lists and dictionaries too deeply. If you're nesting
items much deeper than what you see in the preceding examples or you're
working with someone elses code with significant levels of nesting, most
likely a simpler way to solve the problem exists.
"""
