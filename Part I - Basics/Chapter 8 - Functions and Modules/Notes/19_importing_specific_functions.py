"""
You can also import a specific function from a module. Here's the
general syntax for this approach:

===========================================
| # from module_name import function_name |
===========================================

You can import as many functions as you want from a module by 
separating each function's name with a comma:

=================================================================
| # from module_name import function_0, function_1, function_ 2 |
=================================================================

The making_pizzas.py example would look like this if we want to 
import just the function we're going to use:

===================================
| # from pizza import make_pizza  |
|                                 |
| # make_pizza(16, 'pepperoni)    |
===================================

With this syntax, you don't need to use the dot notation when you
call a function. Because we've explicitly imported the function 
make_pizza() in the import statement, we can call it by name when
we use the function.
"""
