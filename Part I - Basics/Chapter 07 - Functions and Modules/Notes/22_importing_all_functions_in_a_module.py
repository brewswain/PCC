# Try to not use this approach!!!

"""
You can tell Python to import every function in a module by
using the asterisk operator:

=====================================================================
|   # from pizza import *                                           |
|                                                                   |
|   # make_pizza(16, 'pepperoni')                                   |
|   # make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')  |
=====================================================================

The asterisk in the import statement tells Python to copy every function 
from the module pizza into this program file. Because every function is
imported, you can call each function by name without using the dot notation.

However, it's best not to use this approach when you're working with larger
modules that you didn't write: If the module has a function name that matches
an existing name in your project, you can get some unexpected results. Python
may see several functions or variables with the same name, and instead of
importing all the functions separately, it will overwrite the functions.

The best approach is to import the function or functions you want, or import
the entire module and use the dot notation. This leads to clear code that's
easy to read and understand.
"""
