"""
Let's look at a simple error that causes Python to raise an exception. You
probably know that it's impossible to dive a number by zero, but let's ask
Python to do it anyway:
"""

# print(5 / 0)

"""
Of course Python can't do this, so we get a traceback:

============================================
|   # ZeroDivisionError: division by zero  |
============================================

The error reported in the traceback, ZeroDivisionError, is an exception 
object. Python creates this kind of object in response to a situation
where it can't do what we ask it to. When this happens, Python stops
the program and tells us the kind of exception that was raised. We can
use this information to modify our program. We'll tell Python what to 
do when this kind of exception occurs; that way, if it happens again,
we're prepared.
"""

# Using try-except Blocks

"""
When you think an error may occur, you can write a try-except block to
handle the exception that might be raised. You tell Python to try running
some code, and you tell it what to do if the code results in a particular
kind of exception. 

Here's what a try-except block for handling the ZeroDivisionError looks like:
"""

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


"""
We put print(5/0), the line that caused the error, inside a try block. If the
code in a try block works, Python skips over the except block. If the code in
the try block causes an error, Python looks for an except block whose error 
matches the one that was raised and runs the code in that block.

In this example, the code in the try block produces a ZeroDivisionError, so
Python looks for an except block telling it how to respond. Python then runs
the code in that block, ane the user sees a friendly error message instead
of a traceback:

==================================
|   # You can't divide by zero!  |
==================================

If more code followed the try-except block, the program would continue 
running because we told Python how to handle the error.
"""
