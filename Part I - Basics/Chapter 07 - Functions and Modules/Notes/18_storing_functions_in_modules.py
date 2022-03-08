"""
One advantage of functions is the way they separate blocks of
code from your main program. By using descriptive names for 
your functions, your main program wll be much easier to
follow. You can go a step further by storing your functions
in a separate file called a "module" and then importing that
module into your main program. An import statement tells
Python to make the code in a module available in the currently
running program file.

Storing your functions in a separate file allows you to hide the
details of your program's code and focus on its higher-level 
logic. It also allows you to reuse functions in many different programs.
When you store your functions in separate files, you can share
those files with other programmers without having to share your entire
program. Knowing how to import functions also allows you to use 
libraries of functions that other programmers have written. There
are several ways to import a module:
"""

# Importing an Entire Module

r"""
To start importing functions, we first need to create a module. A module
is a file ending in .py that contains the code you want to import into 
your program. Let's make a module that contains the function make_pizza().
(modules\pizza\pizza.py)

Now we'll make a separate file called making_pizzas.py in the same directory 
as pizza.py(modules\pizza\making_pizzas.py). This file imports the module we 
just created and then makes
two calls to make_pizza():

================================================================================
|                                                                              |
|   # Making a 16-inch pizza with the following toppings:                      |
|   # - Pepperoni                                                              |
|                                                                              |
|   # Making a 12-inch pizza with the following toppings:                      |
|   # - Mushrooms                                                              |
|   # - Green Peppers                                                          |
|   # - Extra Cheese                                                           |    
|                                                                              |
================================================================================      

When Python reads this file, the line import pizza tells Python to open the file
pizza.py and copy all the functions from it into this program. You don't actually
see code being copied between files because Python copies the code behind the 
scenes as the program runs. All you need to know is that any function defined in
pizza.py will now be available in making_pizzas.py.

To call a function from an imported module, enter the name of the module you
imported, 'pizza', followed by the name of the function, 'make_pizza()',
separated by a dot:

======================
| pizza.make_pizza() |
======================
This code produces the same output as the original program that didn't import a
module. This first approach to importing, in which you simply write import followed
by the name of the module, makes every function from the module available in your
program. If you use this kind of import statement to import an entire module named
module_name.py, each function in the module is available through the following
syntax:
===============================
| module_name.function_name() |
===============================
"""
