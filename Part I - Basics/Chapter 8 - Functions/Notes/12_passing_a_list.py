"""
You'll often find it useful to pass a list to a function, whether it's a
list of names, numbers, or more complex objects, such as dictionaries.
When you pass a list to a function, the function gets direct access to the
contents of the list. Let's use functions to make working with lists more
efficient.

Say we have a list of users and want to print a greeting to each. The following
example sends a list of names to a function called greet_users(), which
greets each person in the list individually.
"""


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

"""
We define greet_users() so it expects a list of names, which it stores in the 
parameter 'names'. The function loops through the list it receives and prints 
a greeting to each user. We define a list of users and then pass the list
'usernames' to greet_users() in our function call.
"""
