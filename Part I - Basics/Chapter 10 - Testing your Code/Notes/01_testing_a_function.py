"""
To learn about testing, we need code to test. Here's a simple function
that takes in a  first and last name, and returns a neatly formatted
full name:
"""
# name_function.py


def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + " " + last
    return full_name.title()


"""
The function get_formatted_name() combines the first and last name with
a space in between to complete a full name, and then capitalizes and
returns the full name. To check that get_formatted_name() works, let's
make a program that uses this function. the program names.py lets users
enter a first and last name, and see a neatly formatted full name:
"""
# names.py

print("enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

"""
The user can enter a series of first and last names, and see the formatted
full names that are generated:

=============================================
|   # Please give me a first name: brandon  |
|   # Please give me a last name: lee       |
|   # Neatly formatted name: Brandon Lee.   |
=============================================

We can see that the names generated here are correct. But let's say we want
to modify get_formatted_name() so it can also handle middle names. As we do
so, we want to make sure we don't break the way the function handles names 
that only have a first and last name. We could test our code by running
names.py and entering a name like Janis Joplin every time we modify
get_formatted_name(), but that would become tedious. 

Fortunately, Python provides an efficient way to automate the testing of a 
function's output. If we automate the testing of get_formatted_name(), we 
can always be confident that the function will work when given the kinds
of names we've written tests for.
"""
