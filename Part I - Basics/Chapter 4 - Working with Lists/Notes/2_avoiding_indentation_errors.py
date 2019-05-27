"""
Python uses indentation to determine when one line of code is connected to the line above it. 
It's therefore very apparent how important it is to correctly indent your code, else you'll get errors.
There are some common indentation errors that will inevitably crop up, as seen below.
"""

# Forgetting to Indent

# Always indent the line after the for statement in a loop.
# The print statement should be indented, but it's not. This returns a syntax error.


"""
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
print(magician)
"""

# Forgetting to Indent Additional Lines

"""
Sometimes your loop will run without errors but won't produce the expected result. This can
happen when you're trying to do several tasks ina  loop and you forget to indent some lines.
eg:
"""
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(magician.title() + ', that was a great trick!')
print("I can't wait to see your next trick, " + magician.title() + '.\n')


"""
Because the print statement at line 29 was not indented, it is executed only once after the
loop finishes running.
This is called a logical error. The syntax is valid, but because a problem occurs in its logic,
the code does not produce the expected result.
"""

# Indenting Unnecessarily
"""
If you accidentally indent a line that doesn't need to be indented, Python informs you about
the unexpected indent. You can avoid this error by simply only indenting when you have a
specific reason to do so.

Be careful, particularly when indenting code that should be run after a loop has finished,
as this produce a logical error.
"""
