"""
Saving data with json is useful when you're working with user-generated data,
because if you don't store your user's information somehow, you'll lose it
when the program stops running. Let's look at an example where we prompt the
user for their name the first time they run a program and then remember their
name when they run the program again. Let's start by storing the user's name:
"""
# remember_me.py

# import json
# username = input("What is your name? ")

# filename = 'username.json'
# with open(filename, 'w') as file_object:
#     json.dump(username, file_object)
#     print("We'll remember you when you come back, " + username + "!")

"""
At line 11 we prompt for a username to store. Next, we use json.dump(),
passing it a username and a file object, to store the username in a file(line 15).
Then we print a message informing the user that we've stored their information.

Now, let's write a new program that greets a user whose name h8as already been
stored:
"""
# greet_user.py

# import json
# filename = 'username.json'

# with open(filename) as file_object:
#     username = json.load(file_object)
#     print("Welcome back, " + username + "!")

"""
At line 32 we use json.load() to read the information stored in username.json into 
the variable username. Now that we've recovered the username, we can welcome them 
back.

We need to combine these two programs into one file. When someone runs remember_me.py,
we want to retrieve their username from memory if possible; therefore, we'll start
with a try block that attempts to recover the username. If the file username.json doesn't 
exist, we'll have the except block prompt for a username and store it in username.json for
the next time:
"""

# remember_me.py


# Load the username if it has been stored previously.
# Otherwise, prompt for the username and store it.

import json
filename = 'username.json'

try:
    with open(filename) as file_object:
        username = json.load(file_object)
except FileNotFoundError:
    username = input("What is your username? ")
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")

"""
There's no new code here; blocks of code from the last two examples are just combined into
one file. At line 57 we try to open the file username.json. If this file exists, we read 
the username back into memory(line 58) and print a message welcoming back the user in the 
else block. If this is the first time the user runs the program, username.json won't 
exist and a FileNotFoundError will occur. 

Python will then move on to the except block where we prompt the user to enter their username 
(line 60). We then use json.dump() to store the username and print a greeting(line 61).

Whichever block executes, the result is a username and an appropriate greeting. Ifg this is 
the first time the program runs, this is the output:

============================================================
|   # What is your name? bleegeehost                       |
|   # We'll remember you when you come back, bleegeehost!  |
============================================================

Otherwise:

===================================
|   # Welcome back, bleegeehost!  |
===================================

This is the output you see if the program was already run at least once.
"""
