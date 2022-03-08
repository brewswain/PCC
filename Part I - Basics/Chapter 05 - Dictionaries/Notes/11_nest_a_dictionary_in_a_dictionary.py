"""
You can nest a dictionary inside another dictionary, but this
increases code complexity. For example, if you have several
users for a website, each with a unique username, you can
use the usernames as keys in a dictionary. 
Then, you can store ino about each user by using a dictionary
as a value associated with their username.
"""

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}


for username, user_info in users.items():
    print('\nUsername: ' + username)

    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())


"""
We first defined  a dictionary called users with two keys:
one each for the usernames 'aeinstein' and 'mcurie'. The
value associated with each key is a dictionary that includes
first name, last name, and location.

We then loop through the users dictionary, while storing 
each key into the variable username, and the dictionary 
associated with each username goes into the variable
user_info. Once inside the main loop, we print the username.

Then, we start accessing the inner dictionary. The variable
user_info, which contains the dictionary of user information,
has three keys: 'first', 'last', 'location'. We generate a 
nearly formatted full name + location for each person, 
and print a summary of each user.

Although not required, ensuring that the structure of each 
user's dictionary is identical makes nested dictionaries easier
to work with. If each user's dictionary had different key, the
code inside the for loop would be more complicated.
"""
