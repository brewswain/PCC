"""
Think of a class as a set of instructions for how to make an instance.
The class Dog is a set of instructions that tells Python how to make
individual instances representing specific dogs. Let's make an
instance representing a specific dog:
"""


class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


"""
At line 26, we tell Python to create a dog whose name is 'willie'
and whose age is 6. When Python reads this line, it calls the
__init__() method in Dog with the arguments 'willie' and 6.
The __init__() method creates an instance representing this
particular dog and sets the name and age attributes using the
values we provided. The __init__() method has no explicit
return statement, but Python automatically returns an instance
in the variable my_dog.

The naming convention is helpful here:
We can usually assume that a capitalised name like Dog refers to
a class, and a lowercase name like my_dog refers to a single
instance created from a class.
"""

# Accessing Attributes

"""
To access the attributes of an instance, you use dot notation. At
line 28,  we access the value of my_dog's attribute 'name' by 
writing:

==================
|   my_dog.name  |
==================

Dot notation is used often in Python. This syntax demonstrates how
Python finds an attribute's value. Here Python looks at the instance
my_dog and then finds the attribute 'name' associated with my_dog.
This is the same attribute referred to as self.name in the class Dog.

At line 29. we use the same approach to work with the attribute age.
The output is a summary of what we know about my_dog:

=================================
|   # My dog's name is Willie.  |
|   # My dog is 6 years old.    |
=================================

"""
