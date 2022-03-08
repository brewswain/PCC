"""
You can model almost anything using classes. Let's start by writing
a simple class, Dog, that represents a dog - not one dog in
particular, but any dog. What do we know about most pet dogs? Well,
they all have a name and age. We also know that most dogs sit and roll
over. Those two pieces of information(name and age) and those two
behaviours(sit and roll over) will go in our Dog class because they're
common to most dogs.

This class will tell Python how to make an object representing a dog.
After our class is written, we'll use it to make individual instances,
each of which represents one specific dog.

Each instance created from the Dog class will store a name and an age,
and we'll give each dog the ability to sit() and roll_over():
"""

# Creating the Dog Class


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


"""
At line 21 we define a class called 'Dog'. By convention, capitalizzed
names refer to classes in Python. The parentheses in the class definition
are empty because we're creating this class from scratch. We then write a
docstring detailing what this class does. 
"""
