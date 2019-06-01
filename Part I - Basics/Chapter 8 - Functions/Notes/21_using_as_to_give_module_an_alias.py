"""
You can also provide an alias for a module name. Giving a module
a short alias, like p for pizza, allows you to call the module's 
functions more quickly. Calling p.make_pizza() is more concise than
calling pizza.make_pizza():

=======================================================================
|   # import pizza as p                                               |
|                                                                     |
|   # p.make_pizza(16, 'pepperoni)                                    |
|   # p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')  |
=======================================================================

The module pizza is given the alias p in the import statement, but all
of the module's functions retain their original names. Calling the 
functions by writing p.make_pizza() is not only more concise than writing
pizza.make_pizza(), but also redirects your attention from the module name
and allows you to focus on the descriptive names of its functions. These 
function names, which clearly tell you what each function does, are more
important to the readability of your code than using the full module name.

The general syntax for this approach is:

=================================
|   # import module_name as mn  |
=================================

"""
