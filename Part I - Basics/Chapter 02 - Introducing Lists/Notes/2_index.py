"""
As with most programming languages, Python considers the first item in a list to be at position 0.
For accessing the last element in a list, you can use index -1. This is particularly useful if you 
don't know the length of the list. This works with -2, -3 etc as well.
"""


bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print('My first bike was a ' + bicycles[-2].title() + '.')
