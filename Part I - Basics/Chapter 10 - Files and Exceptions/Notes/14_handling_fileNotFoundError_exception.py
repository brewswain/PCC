"""
One common issue when working with files is handling missing files.
The file you're looking for might be in a different location, the 
filename may be misspelled, or the file may not exist at all. You 
can handle all of these situations in a straightforward way with a
try-except block.

Let's try to read a file that doesn't exist. The following program
tries to read in the contents of Alice in Wonderland, but I haven't
saved the file alice.txt in the same directory as alive.py:
"""

# filename = 'alice.txt'

# with open(filename) as file_object:
#     contents = file_object.read()

"""
The last line of the traceback reports a FileNotFoundError: 

================================================================
|   # FileNotFoundError: [Errno 2] No such file or directory:  |
|   # 'alice.txt'                                              |
================================================================

This is the exception Python creates when it can't find the file it's 
trying to open. In this example,  the open() function produces the error, 
so, to handle it, the try block will begin just before the line that 
contains open():
"""

filename = 'alice.txt'

try:
    with open(filename) as file_object:
        contents = file_object.read()

except FileNotFoundError:
    message = "Sorry, the file " + filename + " does not exist."
    print(message)


"""
In this example, the code in the try block produces a FileNotFoundError,
so Python looks for an except block that matches that error. Python then
runs the code in that block, and the result is a friendly error message
instead of a traceback:

=================================================
|   # Sorry, the file alice.txt does not exist  |
=================================================

The program has nothing more to do if the file doesn't exist, so the 
error-handling code doesn't add much to this program. Let's build on this
example and see how exception handling can help when you're working with
more than one file in the next few files.
"""
