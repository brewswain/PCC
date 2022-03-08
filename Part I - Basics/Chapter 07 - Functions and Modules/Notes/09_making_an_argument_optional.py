"""
Sometimes it makes sense to make an argument optional so that people
using the function can choose to provide extra information only if
they want to. You can use default values to make an argument optional.

In the case of if you want to expand on get_formatted_name()
(seen in 8_return_values.py) to give it functionality to handle middle 
names, but make it optional, we can give the middle_name argument an
empty default value and ignore the argument unless the user provides
a value. 

To make this work without a middle name, we set the default value of
middle_name to an empty string and move it to the end of the list of
parameters:
"""


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

"""
Python interprets non-empty strings as True, so 
"if middle_name:" evaluates to true if a middle name argument
is in the function call. If no middle name is provided, the empty string 
fails the if test, causing the else block to run.

Optional values allow functions to handle a wide range of use cases
while letting function calls remain as simple as possible.
"""
