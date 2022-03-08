"""
Because a function definition can have multiple parameters, a function call may need
multiple arguments. You can pass arguments to your functions in a number of ways.

You can use positional arguments, which need to be in the same order the parameters were
written;

Keyword arguments, where each argument consists of a variable name and a value;

And lists and dictionaries of values.
"""

# Positional Arguments

"""
When you call a function, Python must match each argument in the function call with a
parameter in the function definition. The simplest way to do this is based on the order
of the arguments provided. Values matched up this way are called positional arguments.
"""


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'carson')

"""
When we call describe_pet(), we need to provide an animal type and a name, in that order.
In the function body, these two parameters are used to display information about the
pet being described.
"""


# Multiple Function Calls

"""
Calling a function multiple times is a very efficient wy to work. The code describing a pet is
written once in the function. Then, anytime you want to describe a new pet, you call the function
with the new pet's information. Even if the code for describing a pet were to expand to ten lines,
you could still describe a new pet in just one line by calling the function again.

You can use as many positional arguments as you need in your functions. Python works through the
arguments you provide when calling thefunction, and matches each one with the corresponding parameter
in the function's definition.
"""


# Order Matters in Positional Arguments

"""
You can get unexpected results if you mix up the order of the arguments in a function call when
using positional arguments:
"""


def describe_pet_topsy_turvy(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet_topsy_turvy('harry', 'hamster')
describe_pet_topsy_turvy('carson', 'dog')

"""
If you get funny results like this, check to make sure that the order of the arguments in your function call
matches the order of the parameters in the function's definition.
"""
