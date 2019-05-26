# What Is a List?

"""
A list is a collection of items in a particular order. You can make a listthat incldues the letters of the alphabet,
the digits from 0-9, etc. You can put anything you want into a list, and the items in your list don't have to be related in any 
particular way. It's a good idea to make the name of your list plural,  such as letter, digits, or names.

Square brackets indicate a list in python, and the individual elements are separated by commas.
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)


# Accessing Elements in a List

"""
Lists are ordered collections, so individual elements can be accessed by telling Python the position/index of the item desired.
"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0].title())
