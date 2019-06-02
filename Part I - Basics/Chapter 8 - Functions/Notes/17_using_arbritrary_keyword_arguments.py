"""
Sometimes you'll want to accept an arbitrary number of arguments, but 
you won't know ahead of time what kind of information will be passed to
the function. In this case, you can write functions that accept as many
key-value pairs as the calling statement provides. One example involves
building user profiles: You know you'll get information about a user,
but you're not sure what kind of information you'll receive.

The function build_profile() in the following example always takes in a
first and last name, but it accepts an arbitrary number of keyword
arguments as well:
"""


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}

    profile['first_name'] = first
    profile['last_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)


"""
The double asterisks before the parameter **user_info causes Python to 
create an empty dictionary called user_info and pack whatever name-value
pairs it receives into this dictionary. At line 22, we loop through the
additional key-value pairs in the dictionary user_info and add each pair
to the profile dictionary. Finally, we return the profile dictionary to 
the function call line.

You can mix positional, keyword, and arbitrary values in many different 
ways when writing your own functions. It's useful to know that all these
argument types exist because you'll see them often when you start reading
other people's code.
"""
