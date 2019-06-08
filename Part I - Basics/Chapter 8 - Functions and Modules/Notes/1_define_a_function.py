def greet_user():
    """Display a simple greeting."""
    print("Hello!")


greet_user()

"""
This example shows the simplest structure of a function. 
The keyword def informs Python that you're defining a function.
This is the 'function definition', which tells Python the name of 
the function, and, if applicable, what kind of info the function
needs to do its job.

The info is stored in the parentheses. In the example, the name
of the function is greet_user(), and needs no information to do
its job, so its parentheses are empty.(The parentheses are still needed.)


The indented lines that follow def greet_user(): make up the body of
the function. The triple quoted text at line 2 is called a docstring,
which is a comment that describes what the function does. The triple
quotes are important, as Python looks for them when it generates 
documentation for the functions in your programs.

To call a function, you write the name of the function, followed
by any necessary information in parentheses.
"""

# Passing Information to a function

"""
Modified slightly, the function greet_user() can not only tell the
user "hello!" but also greet them by name. For this, you enter
'username' in the parentheses of the function's definition at
def greet_user(). By adding 'username' here, you allow the function
to accept any value of 'username' that you specify.

The function now expects you to provide a value for 'username' each
time you call it. When you call greet_user(), you can pass a name, 
such as 'jesse', inside the parentheses.
"""


def greet_username(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")


greet_username('jesse')
