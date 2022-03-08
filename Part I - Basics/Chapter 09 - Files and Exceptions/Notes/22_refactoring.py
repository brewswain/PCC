"""
Often, you'll come to a point where your code will work, but you'll
recognize that you could improve the code by breaking it up into a
series of functions that have specific jobs. This process is called 
refactoring. Refactoring makes your code cleaner, easier to understand,
and easier to extend.

We can refactor remember_me.py by moving the bulk of its logic into 
one or more functions. The focus of remember_me.py is on greeting the
user, so let's move all our existing code into a function called 
greet_user():
"""

# import json

# def greet_user():
#     """Greet the user by name."""
#     filename = 'username.json'

#     try:
#         with open(filename) as file_object:
#             username = json.load(file_object)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as file_object:
#             json.dump(username, file_object)
#             print("We'll remember you when you come back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")


# greet_user()

"""
Because we're usaing a function now, we update the comments with a docstring
that reflects how the program currently works. This file is a little cleaner, 
but the function greet_user() is doing more than just greeting the user-
It's also retrieving a stored username if one exists and prompting for a new
username if one doesn't exist.

Let's refactor greet_user() so it's not doing so many different tasks. We'll 
start by moving the code for retrieving a stored username to a separate
function:
"""

# import json

# def get_stored_username():
#     """Get stored username if available."""
#     filename = 'username.json'

#     try:
#         with open(filename) as file_object:
#             username = json.load(file_object)
#     except FileNotFoundError:
#         return None
#     else:
#         return username


# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         print("Welcome back, " + username + "!")
#     else:
#         username = input("What is your name? ")
#         filename = 'username.json'

#         with open(filename, 'w') as file_object:
#             json.dump(username, file_object)
#             print("We'll remember you when you come back, " + username + "!")


# greet_user()

"""
The new function get_stored_username() has a clear purpose, as stated in 
its docstring(line 51). This function retrieves a stored username and
returns the username if it finds one. If the file username.json doesn't 
exist, the function returns 'None'(line 58). This is good practice: a function
should either return the value you're expecting, or it should return None. 
This allows hs to performa a simple test with the return value of the function.

At line 66, we print a welcome back message to the user if the attempt to retrieve
a username was successful, and if it doesn't, we prompt for a username.

We should factor one more block of code out greet_user(). If the username doesn't
exist, we should move the code that prompts for a new username to a function 
dedicated to that purpose:
"""




import json
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'

    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'

    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()

"""
Each function in this final version of remember_me.py has a single, clear
purpose. We call greet_user(), and that function prints an appropriate
message: It either welcomes back an existing user or greets a new 
user. It does this by calling get_stored_username(), which is responsible 
only for retrieving a stored username if one exists. 

Finally, greet_user() calls get_new_username() if necessary, which is 
responsible only for getting a new username and storing it This 
compartmentalization of work is an essential part of writing clear code that
will be easy to maintain and extend.
"""
