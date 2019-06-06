"""
The write() function doesn't add any newlines to the text you write. So
if you write more than one line without including newline characters, 
your file may not look the way you want it to:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\programming.txt"

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
    file_object.write('I love creating new games.')


"""
If you open programming.txt, you'll see the two lines squished 
together:

======================================================
|   # I love programming.I love creating new games.  |
======================================================

Including newlines in your write() statements makes each string appear
on its own line:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\programming.txt"

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')


"""
The output now appears on separate lines:

===================================
|   # I love programming.         |
|   # I love creating new games.  |
===================================

You can also use spaces, tab characters, and blank lines to
format your output, just as you've been doing with terminal-based
output.
"""
