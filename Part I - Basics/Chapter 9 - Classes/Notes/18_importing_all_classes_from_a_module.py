"""
You can import every class from a module using the following syntax:

==================================
|   # from module_name import *  |
|   # from car import *          |
==================================

However, this method is not recommended for two reasons. First, it's 
helpful to be able to read the import statements at the top of a file
and get a clear sense of which classes a program uses. With this approach,
it's unclear which classes you're using from the module. 

This approach can also lead to confusion with names in the file. If you accidentally 
import a class with the same name as something else in your program file,
you can create errors that are hard to diagnose. This approach is shown
because, even though it's not a recommended approach, you're likely to 
see it in other people's code.

If you need to import many classes from a module, you're better off importing the entire
module and using the module_name.class_name syntax. You won't see all the classes used
at the top of the file, but you'll see clearly where the module is used in the program.
You'll also avoid the potential naming conflicts that can arise when you import every
class in a  module.
"""
