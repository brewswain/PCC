"""
Because positional arguments, keyword arguments, and default value can
all be used together, often you'll have several equivalent ways to call
a function. Consider the following definition for describe_pets() with
one default value provided:

def describe_pet(pet_name, animal_type='dog')


With this definition, an argument always needs to be provided for 
pet_name, and this value can be provided using the positional or
keyword format. If the animal being described is not a dog, an 
argument for animal_type must be included in the call, and this 
argument can also be specified using the positional or keyword format.

All of the following calls would work for this function:
"""


def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
