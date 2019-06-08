"""
A function doesn't always have to display its output directly. Instead, it
can process some data and then return a value or set of values. The value 
the function returns is called a return value. The return statement takes
a value from inside a function and sends it back to the line that called
the function. Return values allow you to move much of your program's grunt
work into functions, which can simplify the body of your program.
"""

# Returning a Simple Value


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

"""
The definition of get_formatted_name() takes as parameters, a first and last
name. The function combines these two names, adds a space, and stores the 
result in full_name. The value of full_name is converted to title case,
and then returned to the calling line.

When you call a function that returns a value, you need to provide a variable
where the return value can be stored. In this case, the returned value is stored
in the variable musician. The output then shows a neatly formatted name made up
of the parts of a person's name.

Although in this case the process seems convoluted to just get a neatly formatted
name, when you begin working with large programs that needs to store many first
and last names separately, functions like get_formatted_name become super useful.
You store first and last names separately and then call this function whenever you
want to display a full name.
"""
