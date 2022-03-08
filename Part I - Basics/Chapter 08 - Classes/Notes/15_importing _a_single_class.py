# Importing Classes

"""
As you add more functionality to your classes, your files can get long,
even when you use inheritance properly. In keeping with the overall
philosophy of Python, you'll want to keep your files as uncluttered as possible.
To help, Python lets you store classes in modules and then import the classes
you need into your main program.
"""

# Importing a Single Class

"""
Let's create a module containing just the Car class. Please see car.py in the
modules folder of this chapter. We begin by including a module-level docstring
that briefly describes the contents of this module. You should write a docstring
for each module you create.

Now we create a separate file called my_car.py. This file will import the Car
class and then create an instance from that class. Once again, please refer to
the modules folder of this chapter.Please note that my_car.py has some documentation
in the file highlighting the syntax for opening the car module and importing the
Car class.

Importing classes is an effective way to program. Picture how long this program file
would be if the entire Car class were included. When you instead move the class to a
module and import the module, you still get all the same functionality, but you keep
your main program file clean and easy to read. You also store most of the log in 
separate files; once your classes work as you want them to, you can leave those files 
alone and focus on the higher-level logic of your main program.
"""
