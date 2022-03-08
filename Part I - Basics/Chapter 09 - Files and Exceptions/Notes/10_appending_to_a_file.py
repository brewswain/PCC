"""
If you want to add content to a file instead of writing over existing content,
you can open the file in append mode. When you open a file in append mode,
Python doesn't erase the file before returning the file object. Any lines you
write to the file will be added at the end of the file. bIfg the file doesn't
exist yet, Python will create an empty file for you.

Let's modify a file by adding some new reasons we love programming to the
existing file programming.txt:
"""

filename = r"Python_Crash_Course_WIP\Part I - Basics\Chapter 10 - Files and Exceptions\example files\programming.txt"

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

"""
We use the 'a' argument to open the file for appending rather than writing over
the existing file. Then, we write two new lines, which are added to programming.txt:

========================================================
|   # I love programming.                              |
|   # I love creating new games.                       |
|   # I also love finding meaning in large datasets.   |
|   # I love creating apps that can run in a browser.  |
========================================================

We end up with the original contents of the file, followed by the new content we just added.
"""
