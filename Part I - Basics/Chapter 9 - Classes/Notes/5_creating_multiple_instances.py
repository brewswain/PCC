"""
You can create as many instances from a class as you need. Let's
create a second dog called your_dog:
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
your_dog = Dog('lucy', 3)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


"""
In this example we created a dog named Willie, and a dog named Lucy.
Each dog is a separate instance with it's own set of attributes,
capable of the same set of actions:

=================================
|   # My dog's name is Willie.  |
|   # My dog is 6 years old.    |
|   # Willie is now sitting.    |
|                               |
|   # Your dog's name is Lucy.  |   
|   # Your dog is 3 years old.  |
|   # Lucy is now sitting.      |
=================================

Even if we used the same name and age for the second dog, Python would
still create a separate instance from the Dog class. You can make as 
many instances from one class as you need, as long as you give each
instance a unique variable name or it occupies a unique spot in a list
or dictionary.
"""
